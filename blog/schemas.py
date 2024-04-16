from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    author: str
    content: Optional[str]