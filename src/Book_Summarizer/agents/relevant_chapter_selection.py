import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import  Any

import prompts 
from Book_Summarizer.agents.simple_llm import SimpleLLMAgent
from data_classes.chapter_list import ChapterList
from data_classes.book_summarizer_state import BookSummarizerState

class AgentRelevantChaptersSelection(SimpleLLMAgent):
    def __init__(self):
        system_prompt = prompts.RELEVANT_CHAPTERS_SELECTION["system_prompt"]
        user_prompt = prompts.RELEVANT_CHAPTERS_SELECTION["user_prompt"]
        response_class = ChapterList
        super().__init__(system_prompt, user_prompt, response_class)

    def __call__(self, state: BookSummarizerState) -> Any:
        print("State: ", state, "\n SELECTING CHAPTERS") if state.verbose == 1 else None
        
        chapters = state.chapter_titles_all
        chapter_titles_to_summarize = self.agent.invoke({"chapter_list": chapters})
        state.chapter_titles_to_summarize = chapter_titles_to_summarize.chapter_list
        
        return state
