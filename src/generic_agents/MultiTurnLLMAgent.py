import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import constants, utils
from typing import Annotated, List, Tuple, TypedDict, Optional, Any
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from abc import ABC, abstractmethod
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
import os 

class MultiTurnLLMAgent(ABC):
    """Agent that summarizes a section of a book."""
    system_prompt: str # System prompt for the agent
    llm: LLMChain # LLM powering the agent
    prompt_template: ChatPromptTemplate # Prompt given to the agent  
    messages: List[Any] # List of messages to be passed to the agent
    agent: Any # Final agent which is a combination of the prompt and the LLM Chain


    def __init__(self, system_prompt: str):
        self._set_api_key()

        self.system_prompt = system_prompt
        self.llm = ChatOpenAI(model=constants.MODEL_NAME)
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_prompt), 
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        self.messages = []
        self.agent = self.prompt_template | self.llm
    
    def user_prompt(self, prompt_template: str, prompt_args: List[str] = [], response_class: Any = None):
        if len(prompt_args) == 0:
            self.messages.append(
                ("user", prompt_template)
            )
        else:
            self.messages.append(
                ("user", prompt_template.format(**prompt_args))
            )
        
        if response_class is not None:
            self.set_structured_output(response_class)
        else:
            self.remove_structured_output()

        response = self.agent.invoke({"messages": self.messages})
        if response_class is None:
            self.messages.append(AIMessage(content=response.content))
            return response.content
        else:
            self.messages.append(AIMessage(content=str(response)))
            return response
    
    def set_structured_output(self, response_class: Any):
        self.llm = ChatOpenAI(model=constants.MODEL_NAME).with_structured_output(response_class)
        self.agent = self.prompt_template | self.llm
    
    def remove_structured_output(self):
        self.llm = ChatOpenAI(model=constants.MODEL_NAME)
        self.agent = self.prompt_template | self.llm
    
    def reset_messages(self):
        self.messages = []
        self.remove_structured_output()
    
    def _set_api_key(self):
        if not os.getenv("OPENAI_API_KEY") or  not os.getenv("TAVILY_API_KEY"):
            os.environ["OPENAI_API_KEY"] = utils.get_openai_api_key()
            os.environ["TAVILY_API_KEY"] = utils.get_tavily_api_key()
    
    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        pass

if __name__ == "__main__":
    system_prompt = "You are a helpful AI assistant"
    math_solver = MultiTurnLLMAgent(system_prompt)
    print(math_solver.user_prompt("Solve the following equation: 2x + 3 = 7"))
    print(math_solver.user_prompt("What is the value of x?"))