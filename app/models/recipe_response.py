from pydantic import BaseModel


class RecipeResponse(BaseModel):
    id: int
    title: str
    ingredients: str
    instructions: str
