from langchain_core.pydantic_v1 import BaseModel
from typing import List

class ChapterList(BaseModel):
    chapter_list: List[str]
