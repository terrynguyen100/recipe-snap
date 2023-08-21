import openai
import configparser

# Load OpenAI API key from config.ini
config = configparser.ConfigParser()
config.read("config.ini")
openai_api_key = config.get("openai", "api_key")

# Set OpenAI API key
openai.api_key = openai_api_key
models = openai.Model.list()

def get_openai_response(prompt):
    try:
      
        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=prompt,
            max_tokens=1000  # You can adjust this value based on your needs
        )
        return response.choices[0].text
    except Exception as e:
        return str(e)
