from fastapi import FastAPI
from scrape_recipe import scrape_recipe
from openai_req import get_openai_response

app = FastAPI()

sample_url = "https://www.inspiredtaste.net/37475/homemade-chicken-noodle-soup-recipe/"


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/get_recipe")
async def get_recipe():
    try:
        metadata = scrape_recipe(sample_url)
        ingredients = metadata["recipeIngredient"]

        prompt = (
            """
            Here is the list of ingredients with each line is 1 group of ingredient. Each line will be formatted into a key-value pair.
            Analyze each line and format them into a JSON format following this sample: if the line is "2 tablespoons butter, chicken fat or olive oil", then the JSON format will be {"butter, chicken fat or olive oil" : "2 tablespoons}.
            Remember that each line will result in only 1 key-value pair.
            Return the entire list of ingredients as a JSON such as "ingredients" : {}.

            List of ingredients:\n 
            """ +
            "\n".join(ingredients)
        )
        extracted_info = get_openai_response(prompt)

        return {extracted_info}
    except Exception as e:
        return {"Error": str(e)}
