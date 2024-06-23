import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langgraph.constants import Send

from data_classes.book_summarizer_state import BookSummarizerState
from data_classes.book_summarizer_state_summarizer_agent import BookSummarizerStateSummarizerAgent

class AgentChapterRouter():
    def __call__(self, state: BookSummarizerState) -> BookSummarizerState:
        print("State: ", state, "\n SENDING TO SUMMARIZER AGENTS") if state.verbose == 1 else None
        sends = []
        # [Send("summarizer_agent", {"index_chapter_to_summarize": i, "book_summarizer_state": state}) for i in range(len(state.chapters_to_summarize))]
        for i in range(state.num_chapters_to_summarize):
            state_summarizer_agent = BookSummarizerStateSummarizerAgent(index_chapter_to_summarize=i, book_summarizer_state=state)
            sends.append(Send("Section Summarizer", state_summarizer_agent))
        print("Sends: ", sends) if state.verbose == 1 else None
        return sends