from fastapi import FastAPI
from helper.scrape_recipe import scrape_recipe
from helper.openai_req import get_openai_response
from helper.helper import find_recipe_key, check_for_dict

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello" "World"}

        # prompt = (
        #     """
        #     Here is the list of ingredients with each line is 1 group of ingredient. Each line will be formatted into a key-value pair.
        #     Analyze each line and format them into a JSON format following this sample: if the line is "2 tablespoons butter, chicken fat or olive oil", then the JSON format will be "butter, chicken fat or olive oil" : "2 tablespoons.
        #     Remember that each line will result in only 1 key-value pair.
        #     Return the entire list of ingredients as a JSON such as "ingredients" : {}.

        #     List of ingredients:\n 
        #     """ +
        #     "\n".join(ingredients)
        # )
        # extracted_info = get_openai_response(prompt)

@app.get("/get_ingredients")
async def get_ingredients(url: str):
    try:
        metadata = scrape_recipe(url)
        ingredients = find_recipe_key(metadata, "recipeIngredient")
        return {"ingredients": ingredients}
    except Exception as e:
        return {"Error": str(e)}


@app.get("/get_instructions")
async def get_instructions(url: str):
    try:
        metadata = scrape_recipe(url)
        instructions = find_recipe_key(metadata, "recipeInstructions")
        return {"instructions": instructions}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/get_recipe")
async def get_recipe(url: str):
    try:
        metadata = scrape_recipe(url)
        ingredients = find_recipe_key(metadata, "recipeIngredient")
        instructions = find_recipe_key(metadata, "recipeInstructions")
        
        if (check_for_dict(ingredients) and check_for_dict(instructions)):
            return {  
                  "ingredients": ingredients,
                  "instructions": instructions,
                }
        if (check_for_dict(ingredients)):
            return {  
                  "ingredients": ingredients,
                }
        if (check_for_dict(instructions)):
            return {  
                  "instructions": instructions,
                }
                
    except Exception as e:
        return {"Error": str(e)}