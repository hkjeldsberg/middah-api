from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.recipe import Recipe
from app.models.recipe_response import RecipeResponse

router = APIRouter()


@router.get("", response_model=List[RecipeResponse], name="recipes")
def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()
