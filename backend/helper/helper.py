# Since metadata can have nested dictionary,
# we need this helper to traverse the entire dictionary to find the key we want.

def find_recipe_key(data, targetKey):
    if isinstance(data, dict):
        if "recipeIngredient" in data:
            return data[targetKey]
        for key, value in data.items():
            result = find_recipe_key(value, targetKey)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_recipe_key(item, targetKey)
            if result:
                return result
    return None
