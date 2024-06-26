import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_classes.book_summarizer_state import BookSummarizerState

class AgentChaptersLoader():
    def _depth_first_iteration(self, node, chapters):
        if node.content is not None and len(node.content) > 0:
            chapters.append(node)
        for child in node.children:
            self._depth_first_iteration(child, chapters)
        

    # def __call__(self, state: BookSummarizerState) -> BookSummarizerState:
    #     print("State: ", state, "\n LOADING SELECTED CHAPTERS") if state.verbose == 1 else None
    #     chapter_titles_to_summarize = state.chapter_titles_to_summarize
    #     book = state.book
    #     chapter_contents = []
    #     num_chapters_to_summarize = state.num_chapters_to_summarize
    #     print("Num chapters to summarize: ", num_chapters_to_summarize) 

    #     chapter_contents = []
    #     self._depth_first_iteration(book.root_node, chapter_contents)
    #     state.chapters_to_summarize = chapter_contents
    #     print("Chapter contents: ", book.root_node)
    #     return state

    def __call__(self, state: BookSummarizerState) -> BookSummarizerState:
        print("State: ", state, "\n LOADING SELECTED CHAPTERS") if state.verbose == 1 else None
        chapter_titles_to_summarize = state.chapter_titles_to_summarize
        book = state.book
        chapter_contents = []
        num_chapters_to_summarize = state.num_chapters_to_summarize
        print("Num chapters to summarize: ", num_chapters_to_summarize) 

        num_chapters = 0
        for node in book.root_node.children:
            if num_chapters_to_summarize is None or num_chapters < num_chapters_to_summarize:
                if node.title in chapter_titles_to_summarize:
                    chapter_contents.append(node)
                    num_chapters += 1
            else:
                break
        state.chapters_to_summarize = chapter_contents
        print("Chapter contents: ", book.root_node)
        return state

# if __name__ == "__main__":
#     # Load a book 
#     from epub import EPUB
#     import constants
#     book = EPUB(constants.BOOK_PATH)

#     agent = AgentChaptersLoader()
#     chapters = []
#     for node in book.root_node.children:
#         print("Node: ", node.content)
#     agent._depth_first_iteration(book.root_node, chapters)
#     print("Chapters: ", chapters)