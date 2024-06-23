from langchain_core.pydantic_v1 import BaseModel

class Response(BaseModel):
    response: str
