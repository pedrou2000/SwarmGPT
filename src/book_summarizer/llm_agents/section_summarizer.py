import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import  Any

import prompts 
from llm_agents.simple_llm import SimpleLLMAgent
from data_classes.response import Response
from data_classes.chapter_summary import ChapterSummary
from data_classes.book_summarizer_state_summarizer_agent import BookSummarizerStateSummarizerAgent

class AgentSectionSummarizer(SimpleLLMAgent):
    def __init__(self):
        system_prompt = prompts.SECTION_SUMMARIZER["system_prompt"]
        user_prompt = prompts.SECTION_SUMMARIZER["user_prompt"]
        response_class = Response
        super().__init__(system_prompt, user_prompt, response_class)
        
    def __call__(self, state: BookSummarizerStateSummarizerAgent) -> Any:
        print("State: ", state, "\n SUMMARIZING CHAPTER ", str(state.index_chapter_to_summarize)) if state.book_summarizer_state.verbose == 1 else None
        
        # Obtain the chapter to summarize and summarize it with the summarizer agent
        index_chapter_to_summarize = state.index_chapter_to_summarize
        chapters_to_summarize = state.book_summarizer_state.chapters_to_summarize
        chapter_to_summarize = chapters_to_summarize[index_chapter_to_summarize]
        agent_response = self.agent.invoke({"section":  chapter_to_summarize.content})
        summary = agent_response.response
        chapter_summary = ChapterSummary(chapter=chapter_to_summarize, chapter_summary=summary)

        print("\n\n SUMMARY of CHAPTER: ", chapter_to_summarize.title, "\n\n", summary) if state.book_summarizer_state.verbose == 1 else None
        return {"chapter_summaries": [chapter_summary]}