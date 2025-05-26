import json
import os
from models import RecipeBook

# Directory and file paths
DATA_DIR = "./data"
DATA_FILE = os.path.join(DATA_DIR, "recipes.json")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def save_to_file(recipe_book, filename=DATA_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(recipe_book.to_dict(), f, indent=2, ensure_ascii=False)

def load_from_file(filename=DATA_FILE):
    book = RecipeBook()
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                book.load_from_dict(data)
            except json.JSONDecodeError:
                print("⚠️ Warning: Could not load data. JSON is malformed.")
    return book
