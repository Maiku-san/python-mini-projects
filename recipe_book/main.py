from utils import (
    print_menu,
    add_recipe,
    filter_by_category,
    suggest_random,
    find_recipe_by_title,
    edit_recipe,
    delete_recipe,
    list_recipes
)
from storage import load_from_file, save_to_file


def main():
    recipe_book = load_from_file()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_recipe(recipe_book)
        elif choice == "2":
            list_recipes(recipe_book)
        elif choice == "3":
            filter_by_category(recipe_book)
        elif choice == "4":
            suggest_random(recipe_book)
        elif choice == "5":
            find_recipe_by_title(recipe_book)
        elif choice == "6":
            edit_recipe(recipe_book)
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
