import random
from tabulate import tabulate
from rich.console import Console
from models import Recipe

# Setup Rich console
console = Console()

CATEGORIES = ["Breakfast", "Lunch", "Dinner", "Snack", "Dessert", "Drink"]

def print_menu():
    console.print("\n[bold magenta]=== Recipe Book ===[/bold magenta]")
    options = [
        "Add a new recipe",
        "List all recipes",
        "Filter by category",
        "Suggest a random recipe",
        "Find a recipe by name",
        "Edit a recipe",
        "Delete a recipe",
        "Save and exit",
    ]
    for i, option in enumerate(options, 1):
        console.print(f"{i}. {option}")


def add_recipe(recipe_book, title, ingredients, instructions, category):
    if category not in CATEGORIES:
        console.print("⚠️ Invalid category. Adding as 'Uncategorized'.")
        category = "Uncategorized"

    recipe = Recipe(
        title=title,
        ingredients=[i.strip() for i in ingredients],
        instructions=instructions,
        category=category
    )
    success = recipe_book.add_recipe(recipe)
    if success:
        console.print(f"✅ Recipe '{title}' added successfully.")
    else:
        console.print("⚠️ Duplicate recipe. Add aborted.")
    return success

def list_recipes(recipe_book):
    if not recipe_book.recipes:
        return console.print("No recipes found.")
    table_data = [[i, recipe.title, recipe.category] for i, recipe in enumerate(recipe_book.recipes, 1)]
    table_str = tabulate(table_data, headers=["#", "Recipe Name", "Category"], tablefmt="fancy_grid")
    console.print("[bold cyan]Available Recipes[/bold cyan]")
    console.print(table_str)

def edit_recipe(recipe, new_title, new_ingredients, new_instructions, new_category):
    if new_title:
        recipe.title = new_title
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
        console.print(f"🗑️ '{recipe.title}' deleted.")
    else:
        console.print("❎ Delete cancelled.")


def filter_by_category(recipe_book):
    category = input("Enter category to filter by: ").strip()
    filtered = recipe_book.filter_by_category(category)
    if not filtered:
        console.print("No recipes found in that category.")
        return
    for i, r in enumerate(filtered, 1):
        console.print(f"\n{i}. {r.title}")
        console.print(f"   Ingredients: {', '.join(r.ingredients)}")
        console.print(f"   Instructions: {r.instructions}")

def find_recipe_by_title(recipe_book):
    title = input("Enter recipe name/title to search: ").strip()
    r = recipe_book.find_by_title(title)
    if r:
        console.print(f"\n🔍 Found: {r.title} [{r.category}]")
        console.print(f"   Ingredients: {', '.join(r.ingredients)}")
        console.print(f"   Instructions: {r.instructions}")
    else:
        console.print("❌ No recipe found by that name.")

def suggest_random(recipe_book):
    if not recipe_book.recipes:
        console.print("No recipes to suggest.")
        return
    r = random.choice(recipe_book.recipes)
    table_str = tabulate([[r.title, r.ingredients, r.category, r.instructions]], headers=["Recipe Name", "Ingredients", "Category", "Instructions"], tablefmt="fancy_grid")
    console.print("[bold cyan]Suggested Recipe:[/bold cyan]")
    console.print(table_str)
