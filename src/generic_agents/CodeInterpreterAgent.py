import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import constants, utils
from typing import Annotated, List, Tuple, TypedDict, Optional, Any
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from abc import ABC, abstractmethod
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os 
from openai import OpenAI
from langchain_core.pydantic_v1 import BaseModel
  
class MathProblemSolution(BaseModel):
    final_solution: str

class CodeInterpreterAgent():
    """ Agent that uses the Assistant API to interact with the user using the code interpreter tool. """
    system_prompt: str # System prompt for the agent
    agent: Any # Final agent which is a combination of the prompt and the LLM Chain
    client: OpenAI # OpenAI client
    thread: Any # OpenAI thread which mantains the conversation with the asssistants agent

    def __init__(self, system_prompt: str, agent_name: str = constants.MODEL_NAME + "_CodeInterpreterAgent"):
        self._set_api_key()
        self.client = OpenAI()
        self.system_prompt = system_prompt

        self.agent = self.client.beta.assistants.create(
            name=agent_name,
            instructions=self.system_prompt,
            tools=[{"type": "code_interpreter"}],
            model=constants.MODEL_NAME,
        )
        self.thread = self.client.beta.threads.create()
    
    def user_prompt(self, prompt_template: str, prompt_args: List[str] = []):
        if len(prompt_args) == 0:
            self.client.beta.threads.messages.create(thread_id=self.thread.id, role="user", content=prompt_template)
        else:
            self.client.beta.threads.messages.create(thread_id=self.thread.id, role="user", content=prompt_template.format(**prompt_args))
        
        response = self.run_agent()

        return response.content[0].text.value

    def run_agent(self):        
        # Once the message is already stored, run the agent
        run = self.client.beta.threads.runs.create(thread_id=self.thread.id, assistant_id=self.agent.id)      
        while run.status in ["queued", "in_progress"]:
            keep_retrieving_run = self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run.id)

            if keep_retrieving_run.status == "queued" or keep_retrieving_run.status == "in_progress":
                pass
            
            elif keep_retrieving_run.status == "completed":
                all_messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
                try:
                    return all_messages.data[0]
                except Exception as e:
                    print(f"Error: {e}")
                    return None
            else:
                print(f"Run status: {keep_retrieving_run.status}")
                return None
    
    def _escape_curly_braces(self, text: str) -> str:
        """Escape curly braces in the given text."""
        return text.replace("{", "{{").replace("}", "}}")
    
    def structured_output(self, response_class: Any, system_prompt: str, message: str):
        message = self._escape_curly_braces(message)

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt), 
                ("user", message),
            ]
        )
        llm = ChatOpenAI(model=constants.MODEL_NAME).with_structured_output(response_class)
        agent = prompt_template | llm
        response = agent.invoke({})
        return response

    def _set_api_key(self):
        if not os.getenv("OPENAI_API_KEY") or  not os.getenv("TAVILY_API_KEY"):
            os.environ["OPENAI_API_KEY"] = utils.get_openai_api_key()
            os.environ["TAVILY_API_KEY"] = utils.get_tavily_api_key()
    
    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        pass


if __name__ == "__main__":
    system_prompt = "You are a personal math tutor. Write and run code to answer math questions."
    math_solver = CodeInterpreterAgent(system_prompt)
    response = math_solver.user_prompt("Solve the following equation: 46439x^5 - 9834834 = 75646363. Give me a final number for the real solution")
    print(response)
    # print(math_solver.user_prompt("Can you repeat what was the solution for the equation?"))

    system_prompt_structured = """
        You are a parser. You are given some unstructured output from another LLM an your task is to structure it in 
        the class format. The class should have a single attribute called final_solution
    """
    print(math_solver.structured_output(MathProblemSolution, system_prompt_structured, response))