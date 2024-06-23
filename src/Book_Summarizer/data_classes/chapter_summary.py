import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.pydantic_v1 import BaseModel, Field
from epub_parser import ContentNode

class ChapterSummary(BaseModel):
    chapter: ContentNode # Chapter Object 
    chapter_summary: str # Summary of the chapter
    
    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary types such as EPUB


if __name__ == "__main__":
    chapter = ContentNode("Chapter 1", "This is the content of the chapter")
    chapter_summary = "This is a summary of the chapter"
    summary = ChapterSummary(chapter=chapter, chapter_summary=chapter_summary)
    print(summary)