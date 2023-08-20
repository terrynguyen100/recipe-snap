import requests
from bs4 import BeautifulSoup
import json

def scrape_recipe(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        json_ld_script = soup.find('script', type='application/ld+json')
        
        if json_ld_script:
            recipe_data = json.loads(json_ld_script.string)
            return recipe_data
        else:
            itemprop_elements = soup.find_all(attrs={"itemprop": True})
            metadata = {}
            for element in itemprop_elements:
                prop_name = element.attrs["itemprop"]
                prop_value = element.get_text()
                metadata[prop_name] = prop_value
            return metadata
    
    except requests.exceptions.RequestException as req_err:
        raise Exception("Error fetching URL:", req_err)
    except (ValueError, KeyError, TypeError) as json_err:
        raise Exception("Error parsing JSON-LD or Microdata:", json_err)
    except Exception as e:
        raise Exception("Error:", e)
