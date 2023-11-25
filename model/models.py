# app/models.py

from main import List, Optional, BaseModel, random

class Token(BaseModel):
    accessToken: str
    tokenType: str

class TokenData(BaseModel):
    username: str = None 

class HighlightModel(BaseModel):
    name: str
    description: str

class PostModel(BaseModel):
    postId: Optional[int] = random.randint(1, 1000000)
    title: str
    content: str
    highlights: List[HighlightModel]
    tips: List[str]

class UpdateHLModel(BaseModel):
    name: Optional[str]
    description: Optional[str]

class UpdateModel(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    highlights: List[UpdateHLModel] = []
    tips: List[str] = []

class UpdateModelWithoutHighlight(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tips: Optional[List[str]] = None

class UpdateModelWithHighlight(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    highlights: Optional[List[UpdateHLModel]] = None
    tips: Optional[List[str]] = None