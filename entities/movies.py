from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int
    name: str = Field(max_length=100, min_length=2, title="Movie Name", description="Name of the movie", example="The Godfather")
    year: int = Field(gt=1900, lt=2022, title="Release Year", description="Year the movie was released", example=1972)
    director: str = Field(max_length=100, min_length=2, title="Director", description="Name of the director", example="Francis Ford Coppola")
    category: str = Field(max_length=100, min_length=2, title="Category", description="Category of the movie", example="Crime")