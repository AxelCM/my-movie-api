from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    name: str
    year: int
    director: str
    category: str