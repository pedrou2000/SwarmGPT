import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from book_summarizer.data_classes.epub import EPUB
from data_classes.book_summarizer_state import BookSummarizerState

class AgentEpubLoader():
    def __call__(self, state: BookSummarizerState) -> BookSummarizerState:
        print("State: ", state, "\n SAVING SUMMARY") if state.verbose == 1 else None
        book = EPUB(state.book_path)
        
        chapter_titles_all = []
        for node in book.root_node.children:
            chapter_titles_all.append(node.title)
        
        state.book = book
        state.chapter_titles_all = chapter_titles_all

        print("\n\n "+str(len(chapter_titles_all))+" chapters found in the book") 

        if state.num_chapters_to_summarize is None:
            state.num_chapters_to_summarize = len(chapter_titles_all)

        return state