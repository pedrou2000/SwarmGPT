import constants
from typing import Annotated, List, Tuple, TypedDict, Optional, Any
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class SimpleLLMAgent():
    """Agent that summarizes a section of a book."""
    system_prompt: str # System prompt for the agent
    user_prompt: str # User prompt for the agent
    response_class: Any # Response class for the agent
    llm: LLMChain # LLM powering the agent
    prompt_template: ChatPromptTemplate # Prompt given to the agent 
    agent: Any # Final agent which is a combination of the prompt and the LLM Chain


    def __init__(self, system_prompt: str, user_prompt: str, response_class: Any):
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.response_class = response_class
        self.llm = ChatOpenAI(model=constants.MODEL_NAME).with_structured_output(response_class)
        self.prompt_template = ChatPromptTemplate.from_messages(
            [("system", self.system_prompt), ("user", self.user_prompt)]
        )
        self.agent = self.prompt_template | self.llm