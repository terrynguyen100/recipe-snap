# import openai
# import configparser
# import json

# # Load OpenAI API key from config.ini
# config = configparser.ConfigParser()
# config.read("config.ini")
# openai_api_key = config.get("openai", "api_key")

# # Set OpenAI API key
# openai.api_key = openai_api_key
# models = openai.Model.list()


# def get_openai_response(prompt):
#     try:

#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             max_tokens=1000
#         )
#         return response.choices[0].message
#     except Exception as e:
#         return str(e)
