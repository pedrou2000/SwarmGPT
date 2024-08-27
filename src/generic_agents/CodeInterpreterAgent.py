import os, sys, time
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

class CodeInterpreterAgent:
    """ Agent that uses the Assistant API to interact with the user using the code interpreter tool. """
    _instance = None
    _initialized = False  # Class-level attribute to track initialization
    
    system_prompt: str # System prompt for the agent
    agent: Any # Final agent which is a combination of the prompt and the LLM Chain
    client: OpenAI # OpenAI client
    thread: Any # OpenAI thread which maintains the conversation with the assistant's agent

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super(CodeInterpreterAgent, cls).__new__(cls)
    #     return cls._instance

    def __init__(self, system_prompt: str, agent_name: str = constants.MODEL_NAME + "_CodeInterpreterAgent"):
        self._initialize(system_prompt, agent_name)
        # self.__class__.__initialized = True  # Mark as initialized

    def _initialize(self, system_prompt: str, agent_name: str):
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
        # self._initialized = True
        # print("\n\n\nInitializing CodeInterpreterAgent with thread id: ", self.thread, "\n\n\n")
    
    def get_number_messages(self):
        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        return len(messages.data)
    
    def get_last_message(self):
        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        return messages.data[0].content
    
    def delete_all_messages(self):
        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        for message in messages.data:
            self.client.beta.threads.messages.delete(thread_id=self.thread.id, message_id=message.id)
        
    def reset_thread(self):
        self.thread = self.client.beta.threads.create()

    def user_prompt(self, prompt_template: str, prompt_args: List[str] = []):
        message = self._prompt_agent(prompt_template, prompt_args)        
        response = self._run_agent()
        return response.content[0].text.value    
    
    def test_human_eval_solutions(self, solution_file_path: str, test_code:str, method_name: str, test_file_save_path=None):
        with open(solution_file_path, "r") as file:
            solution_code = file.read()
        test_program = solution_code + '\n\n' + test_code + '\n\n' + 'check(' + method_name + ')'
        if test_file_save_path:
            with open(test_file_save_path, "w") as file:
                file.write(test_program)
        
        return self.run_code(test_program)

    def run_code_from_file(self, file_path: str = "output.py"):
        # Check if the file exists and is not empty
        if not os.path.exists(file_path) or os.path.getsize(file_path) <= 0:
            return False
        
        # Open the file and check if it has any content
        with open(file_path, "r") as file:
            file_content = file.read()
            if not file_content:
                return False
        return self.run_code(file_content)

    def run_code(self, code: str):
        # Run the code in the file with the exec function and check if it raises any exceptions
        try:
            exec(code)
        except AssertionError as ae:
            print(f"AssertionError in check_code_execution: {ae}")
            return False
        except Exception as e:
            print(f"Error in check_code_execution: {e}")
            return False
        
        return True

    def prompt_with_output_file(self, prompt_template: str, prompt_args: List[str] = [], file_path: str = "output.py"):
        message = self._prompt_agent(prompt_template, prompt_args)        
        response = self._run_agent(n_attempts=3)

        n_attachments = len(response.attachments)

        if n_attachments == 0:
            print("No attachments found in prompt_with_output_file")
            return None
        elif n_attachments > 1:
            print("More than one attachment found in prompt_with_output_file")
            return None

        attachment = response.attachments[0]    
        file_id = attachment.file_id
        n_bytes = self.download_file(file_id, file_path=file_path)
        if n_bytes <= 0:
            print("Error downloading file in prompt_with_output_file")
            return None

        return response.content[0].text.value

    def download_file(self, file_id: str, file_path: str = "test.py"):
        file_data = self.client.files.content(file_id)
        file_data_bytes = file_data.read()
        with open(file_path, "wb") as file:
            return file.write(file_data_bytes)     

    def _prompt_agent(self, prompt_template: str, prompt_args: List[str] = [], n_attempts=3):
        ret = None
        attempt = 1
        while ret is None and attempt <= n_attempts:
            try:
                if len(prompt_args) == 0:
                    ret = self.client.beta.threads.messages.create(thread_id=self.thread.id, role="user", content=prompt_template)
                else:
                    ret = self.client.beta.threads.messages.create(thread_id=self.thread.id, role="user", content=prompt_template.format(**prompt_args))
            except Exception as e:
                print(f"Error in _prompt_agent: {e}")
                ret = None
                attempt += 1
                time.sleep(1)
        return ret
        
    def _run_agent(self, n_attempts=3):
        for i in range(n_attempts):
            response = self._single_run_agent()
            if response is not None and hasattr(response.content[0], 'text'):
                return response
            else:
                print(f"Attempt {i} failed")
        print(f"Failed to run agent after {n_attempts} attempts")
        return response

    def _single_run_agent(self, n_attempts=3):        
        # Once the message is already stored, run the agent
        run = None
        attempt = 1
        while run is None and attempt <= n_attempts:
            try:
                run = self.client.beta.threads.runs.create(thread_id=self.thread.id, assistant_id=self.agent.id)      
            except Exception as e:
                print(f"Error in _prompt_agent: {e}")
                ret = None
                attempt += 1
                time.sleep(1)

        while run.status in ["queued", "in_progress"]:
            keep_retrieving_run = self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run.id)

            if keep_retrieving_run.status == "queued" or keep_retrieving_run.status == "in_progress":
                # Sleep for 1 second
                time.sleep(1)
                pass
            
            elif keep_retrieving_run.status == "completed":
                all_messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
                try:
                    return all_messages.data[0]
                except Exception as e:
                    print(f"_run_agent Failed. Error: {e}")
                    return None
            else:
                print(f"_run_agent Failed. Run status: {keep_retrieving_run.status}")
                return None
        print('_run_agent Failed. Run status: {keep_retrieving_run.status}')
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