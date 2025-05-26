from models import Recipe
import random

CATEGORIES = ["Breakfast", "Lunch", "Dinner", "Snack", "Dessert", "Drink"]

def print_menu():
    print("\n=== Recipe Book ===")
    print("1. Add a new recipe")
    print("2. List all recipes")
    print("3. Filter by category")
    print("4. Suggest a random recipe")
    print("5. Find a recipe by name")
    print("6. Edit a recipe")
    print("7. Delete a recipe")
    print("8. Save and exit")

def add_recipe(recipe_book):
    name = input("Recipe name: ").strip()
    ingredients = input("Ingredients (comma separated): ").split(",")
    instructions = input("Instructions: ").strip()

    print(f"Available categories: {', '.join(CATEGORIES)}")
    category = input("Category: ").strip()
    if category not in CATEGORIES:
        print("⚠️ Invalid category. Adding as 'Uncategorized'.")
        category = "Uncategorized"

    recipe = Recipe(
        title=name,
        ingredients=[i.strip() for i in ingredients],
        instructions=instructions,
        category=category
    )

    success = recipe_book.add_recipe(recipe)
    if success:
        print(f"✅ Recipe '{name}' added successfully.")
    else:
        print("⚠️ Duplicate recipe. Add aborted.")

def edit_recipe(recipe_book):
    title = input("Enter the name of the recipe to edit: ").strip()
    recipe = recipe_book.find_by_title(title)
    if not recipe:
        print("❌ Recipe not found.")
        return

    print("Leave any field empty to keep current value.")
    
    new_name = input(f"New name [{recipe.title}]: ").strip()
    new_ingredients = input("New ingredients (comma-separated): ").strip()
    new_instructions = input("New instructions: ").strip()
    new_category = input(f"New category [{recipe.category}]: ").strip()

    if new_name:
        recipe.title = new_name
    if new_ingredients:
        recipe.ingredients = [i.strip() for i in new_ingredients.split(",")]
    if new_instructions:
        recipe.instructions = new_instructions
    if new_category:
        recipe.category = new_category

    print(f"✅ '{recipe.title}' updated.")

def delete_recipe(recipe_book):
    title = input("Enter the name of the recipe to delete: ").strip()
    recipe = recipe_book.find_by_title(title)
    if not recipe:
        print("❌ Recipe not found.")
        return

    confirm = input(f"Are you sure you want to delete '{recipe.title}'? (y/n): ").strip().lower()
    if confirm == 'y':
        recipe_book.recipes.remove(recipe)
        print(f"🗑️ '{recipe.title}' deleted.")
    else:
        print("❎ Delete cancelled.")

def list_recipes(recipe_book):
    if not recipe_book.recipes:
        print("No recipes found.")
        return
    for i, r in enumerate(recipe_book.recipes, 1):
        print(f"\n{i}. {r.title} [{r.category}]")
        print(f"   Ingredients: {', '.join(r.ingredients)}")
        print(f"   Instructions: {r.instructions}")

def filter_by_category(recipe_book):
    category = input("Enter category to filter by: ").strip()
    filtered = recipe_book.filter_by_category(category)
    if not filtered:
        print("No recipes found in that category.")
        return
    for i, r in enumerate(filtered, 1):
        print(f"\n{i}. {r.title}")
        print(f"   Ingredients: {', '.join(r.ingredients)}")
        print(f"   Instructions: {r.instructions}")

def find_recipe_by_title(recipe_book):
    title = input("Enter recipe name/title to search: ").strip()
    r = recipe_book.find_by_title(title)
    if r:
        print(f"\n🔍 Found: {r.title} [{r.category}]")
        print(f"   Ingredients: {', '.join(r.ingredients)}")
        print(f"   Instructions: {r.instructions}")
    else:
        print("❌ No recipe found by that name.")

def suggest_random(recipe_book):
    if not recipe_book.recipes:
        print("No recipes to suggest.")
        return
    r = random.choice(recipe_book.recipes)
    print(f"\n✨ Suggested Recipe: {r.title}")
    print(f"   Category: {r.category}")
    print(f"   Ingredients: {', '.join(r.ingredients)}")
    print(f"   Instructions: {r.instructions}")
