import json

class Recipe:
    def __init__(self, title, ingredients, instructions, category=None):
        self.title = title
        self.ingredients = ingredients  # List of strings
        self.instructions = instructions  # String
        self.category = category or "Uncategorized"

    def to_dict(self):
        return {
            "title": self.title,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            ingredients=data["ingredients"],
            instructions=data["instructions"],
            category=data.get("category", "Uncategorized")
        )

class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        existing = self.find_by_exact_title(recipe.title)
        if existing:
            print(f"A recipe titled '{recipe.title}' already exists.")
            return False
        self.recipes.append(recipe)
        return True

    def find_by_title(self, keyword):
        for recipe in self.recipes:
            if keyword.lower() == recipe.title.lower():
                return recipe
        return None

    def find_by_exact_title(self, title):
        for recipe in self.recipes:
            if recipe.title.lower() == title.lower():
                return recipe
        return None

    def filter_by_category(self, category):
        return [r for r in self.recipes if r.category.lower() == category.lower()]

    def to_dict(self):
        return [r.to_dict() for r in self.recipes]

    def load_from_dict(self, data_list):
        self.recipes = [Recipe.from_dict(d) for d in data_list]
