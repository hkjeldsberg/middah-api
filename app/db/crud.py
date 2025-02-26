from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.main import app
from app.models.recipe import Recipe


@app.get("/recipes/")
def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()


@app.post("/recipes/")
def create_recipe(recipe: Recipe, db: Session = Depends(get_db)):
    db.add(recipe)
    db.commit()
    return {"message": "Recipe added"}
