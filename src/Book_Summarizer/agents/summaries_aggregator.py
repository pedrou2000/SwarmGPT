import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import  Any

import prompts 
from Book_Summarizer.agents.simple_llm import SimpleLLMAgent
from data_classes.response import Response
from data_classes.book_summarizer_state import BookSummarizerState

class AgentSummariesAggregator(SimpleLLMAgent):
    def __init__(self):
        system_prompt = prompts.SUMMARIES_AGGREGATOR["system_prompt"]
        user_prompt = prompts.SUMMARIES_AGGREGATOR["user_prompt"]
        response_class = Response
        super().__init__(system_prompt, user_prompt, response_class)

    def __call__(self, state: BookSummarizerState) -> Any:
        print("State: ", state, "\n AGGREGATING CHAPTERS") if state.verbose == 1 else None

        # Construct the string to submit to the summaries aggregator agent
        chapter_summaries = ""
        for chapter_summary in state.chapter_summaries:
            chapter_summaries += "Chapter: " + chapter_summary.chapter.title + "\nSummary: " + chapter_summary.chapter_summary + "\n\n"
        
        # Summarize the complete book
        agent_response = self.agent.invoke({"text": chapter_summaries})
        state.final_summary = agent_response.response

        print("\n\nFINAL SUMMARY: \n\n", agent_response.response) if state.verbose == 1 else None
        return state