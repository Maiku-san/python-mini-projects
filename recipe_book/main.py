from utils import (
    print_menu,
    add_recipe,
    filter_by_category,
    suggest_random,
    find_recipe_by_title,
    edit_recipe,
    delete_recipe,
    list_recipes,
    CATEGORIES
)
from storage import load_from_file, save_to_file


def main():
    recipe_book = load_from_file()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            title = input("Recipe name: ").strip()
            ingredients = input("Ingredients (comma separated): ").split(",")
            instructions = input("Instructions: ").strip()
            print(f"Available categories: {', '.join(CATEGORIES)}")
            category = input("Category: ").strip()

            add_recipe(recipe_book, title, ingredients, instructions, category)
        elif choice == "2":
            list_recipes(recipe_book)
        elif choice == "3":
            filter_by_category(recipe_book)
        elif choice == "4":
            suggest_random(recipe_book)
        elif choice == "5":
            find_recipe_by_title(recipe_book)
        elif choice == "6":
            title = input("Enter the name of the recipe to edit: ").strip()
            recipe = recipe_book.find_by_title(title)
            if not recipe:
                print("❌ Recipe not found.")
                continue
            print("Leave any field empty to keep current value.")
            new_title = input(f"New name [{recipe.title}]: ").strip()
            new_ingredients = input("New ingredients (comma-separated): ").strip()
            new_instructions = input("New instructions: ").strip()
            new_category = input(f"New category [{recipe.category}]: ").strip()
            edit_recipe(recipe, new_title, new_ingredients, new_instructions, new_category)
        elif choice == "7":
            delete_recipe(recipe_book)
        elif choice == "8":
            save_to_file(recipe_book)
            print("📘 Recipe book saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
