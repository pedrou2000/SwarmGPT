import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.pydantic_v1 import BaseModel, Field
import operator 
from typing import Annotated, List, Optional

from book_summarizer.data_classes.epub import EPUB, ContentNode
from data_classes.chapter_summary import ChapterSummary

class BookSummarizerState(BaseModel):
    book_name: Annotated[str, Field(description="Name of the book")]  # Name of the book
    verbose: int  # Verbosity level: 0 (silent), 1 (verbose)
    book_dir: str  # Directory of the book
    book: Optional[EPUB] = None  # EPUB object
    chapter_titles_all: List[str] = []  # List of all chapter titles
    chapter_titles_to_summarize: List[str] = []  # List of chapter titles to summarize
    chapters_to_summarize: List[ContentNode] = []  # List of the chapters to summarize
    num_chapters_to_summarize: int  # Number of chapters to summarize
    chapter_summaries: Annotated[List[ChapterSummary], operator.add] = []  # List of summaries of the chapters
    final_summary: str = ""  # Final summary of the book
    summaries_dir: str  # Directory to save the summaries

    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary types such as EPUB

