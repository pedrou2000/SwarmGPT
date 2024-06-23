import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.pydantic_v1 import BaseModel, Field

from epub_parser import ContentNode
from data_classes.book_summarizer_state import BookSummarizerState

class BookSummarizerStateSummarizerAgent(BaseModel):
    index_chapter_to_summarize: int # Index of the chapter to summarize
    book_summarizer_state: BookSummarizerState # State of the book summarizer
