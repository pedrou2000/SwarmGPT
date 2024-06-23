import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_classes.book_summarizer_state import BookSummarizerState

class AgentChaptersLoader():
    def __call__(self, state: BookSummarizerState) -> BookSummarizerState:
        print("State: ", state, "\n LOADING SELECTED CHAPTERS") if state.verbose == 1 else None
        chapter_titles_to_summarize = state.chapter_titles_to_summarize
        book = state.book
        chapter_contents = []
        num_chapters_to_summarize = state.num_chapters_to_summarize

        num_chapters = 0
        for node in book.root_node.children:
            if num_chapters < num_chapters_to_summarize:
                if node.title in chapter_titles_to_summarize:
                    chapter_contents.append(node)
                    num_chapters += 1
            else:
                break
        state.chapters_to_summarize = chapter_contents
        return state