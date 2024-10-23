import json
import sys

try:
    with open(r"categories.txt", 'r', encoding='utf-8') as file:
        categories = json.load(file)

except json.JSONDecodeError as e:
    print(f"Error loading 'categories.txt' file: {e}")
    sys.exit()

except FileNotFoundError as e:
    print(f"Can't locate the 'categories.txt file: {e}")
    sys.exit()

def create_new_category(new_category):
    categories.append(new_category)
    try:
        with open(r"categories.txt", 'w', encoding='utf-8') as file:
            json.dump(categories, file)
            if new_category in categories:

                return True
            else:
                return False
    except:
        return False
    

def set_default_category(default_category):
    try:
        categories.remove(default_category)
        categories.insert(0, default_category)
        with open(r"categories.txt", 'w', encoding='utf-8') as file:
            json.dump(categories, file)
            print(f"Category '{default_category}' set as default...")
        return True

    except:
        return False