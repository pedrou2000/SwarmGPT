import constants, utils
from typing import Annotated, List, Tuple, TypedDict, Optional, Any
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from abc import ABC, abstractmethod
import os 

class SimpleLLMAgent(ABC):
    """Agent that summarizes a section of a book."""
    system_prompt: str # System prompt for the agent
    user_prompt: str # User prompt for the agent
    response_class: Any # Response class for the agent
    llm: LLMChain # LLM powering the agent
    prompt_template: ChatPromptTemplate # Prompt given to the agent 
    agent: Any # Final agent which is a combination of the prompt and the LLM Chain


    def __init__(self, system_prompt: str, user_prompt: str, response_class: Any = None):
        self._set_api_key()

        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.response_class = response_class
        if response_class is not None:
            self.llm = ChatOpenAI(model=constants.MODEL_NAME).with_structured_output(response_class)
        else:
            self.llm = ChatOpenAI(model=constants.MODEL_NAME)
        self.prompt_template = ChatPromptTemplate.from_messages(
            [("system", self.system_prompt), ("user", self.user_prompt)]
        )
        self.agent = self.prompt_template | self.llm
    
    def _set_api_key(self):
        if not os.getenv("OPENAI_API_KEY") or  not os.getenv("TAVILY_API_KEY"):
            os.environ["OPENAI_API_KEY"] = utils.get_openai_api_key()
            os.environ["TAVILY_API_KEY"] = utils.get_tavily_api_key()
    
    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        pass