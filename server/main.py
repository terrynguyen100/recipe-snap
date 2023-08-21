from fastapi import FastAPI
from scrape_recipe import scrape_recipe
from helper import find_recipe_key, check_for_dict
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "Please go to /docs to see the API documentation"}

# @app.get("/get_ingredients")
# async def get_ingredients(url: str):
#     try:
#         metadata = scrape_recipe(url)
#         ingredients = find_recipe_key(metadata, "recipeIngredient")
#         return {"ingredients": ingredients}
#     except Exception as e:
#         return {"Error": str(e)}

# @app.get("/get_instructions")
# async def get_instructions(url: str):
#     try:
#         metadata = scrape_recipe(url)
#         instructions = find_recipe_key(metadata, "recipeInstructions")
#         return {"instructions": instructions}
#     except Exception as e:
#         return {"Error": str(e)}

@app.get("/get_recipe")
async def get_recipe(url: str):
    try:
        metadata = scrape_recipe(url)
        ingredients = find_recipe_key(metadata, "recipeIngredient")
        instructions = find_recipe_key(metadata, "recipeInstructions")
        
        if check_for_dict(ingredients) and check_for_dict(instructions):
            return {  
                  "ingredients": ingredients,
                  "instructions": instructions,
                }
        if check_for_dict(ingredients):
            return {  
                  "ingredients": ingredients,
                }
        if check_for_dict(instructions):
            return {  
                  "instructions": instructions,
                }
                
    except Exception as e:
        return {"Error": str(e)}