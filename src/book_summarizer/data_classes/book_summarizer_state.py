import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.pydantic_v1 import BaseModel, Field
import operator 
from typing import Annotated, List, Optional

from data_classes.epub import EPUB, ContentNode
from data_classes.chapter_summary import ChapterSummary

class BookSummarizerState():
    book_name: Annotated[str, Field(description="Name of the book")]  # Name of the book
    verbose: int  # Verbosity level: 0 (silent), 1 (verbose)
    book_path: str  # Directory of the book
    book: Optional[EPUB] = None  # EPUB object
    chapter_titles_all: List[str] = []  # List of all chapter titles
    chapter_titles_to_summarize: List[str] = []  # List of chapter titles to summarize
    chapters_to_summarize: List[ContentNode] = []  # List of the chapters to summarize
    num_chapters_to_summarize: Optional[int] = None   # Number of chapters to summarize, None means all
    chapter_summaries: Annotated[List[ChapterSummary], operator.add] = []  # List of summaries of the chapters
    final_summary: str = ""  # Final summary of the book
    summaries_dir: str  # Directory to save the summaries

    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary types such as EPUB

    def __init__(
            self, book_name, book_path, num_chapters_to_summarize, summaries_dir, verbose=1,
            book=None, chapter_titles_all=[], chapter_titles_to_summarize=[], chapters_to_summarize=[],
            chapter_summaries=[], final_summary=""
        ):
        self.book_name = book_name
        self.book_path = book_path
        self.summaries_dir = summaries_dir
        self.num_chapters_to_summarize = num_chapters_to_summarize  
        self.verbose = verbose
        if book is not None:
            self.book = book
        if chapter_titles_all is not None and len(chapter_titles_all) > 0:
            self.chapter_titles_all = chapter_titles_all
        if chapter_titles_to_summarize is not None and len(chapter_titles_to_summarize) > 0:
            self.chapter_titles_to_summarize = chapter_titles_to_summarize
        if chapters_to_summarize is not None and len(chapters_to_summarize) > 0:
            self.chapters_to_summarize = chapters_to_summarize
        if chapter_summaries is not None and len(chapter_summaries) > 0:
            self.chapter_summaries = chapter_summaries
        if final_summary is not None and len(final_summary) > 0:
            self.final_summary = final_summary

if __name__ == "__main__":
    state = BookSummarizerState(book_name="Test", verbose=1, book_path="test", summaries_dir="test")
    print(state)
    print(state.dict())