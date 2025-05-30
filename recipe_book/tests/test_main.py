import pytest
from unittest.mock import patch
from main import main
from models import RecipeBook


@pytest.fixture
def recipe_book():
    # Create a new RecipeBook object for each test
    return RecipeBook()

def test_main_add_and_exit(monkeypatch, recipe_book):
    # Simulate user input: choose to add a recipe, provide details, then exit
    inputs = iter([
        "1",             # Add recipe
        "Pasta",         # Recipe name
        "noodles,tomato",# Ingredients
        "Boil and mix",  # Instructions
        "Dinner",        # Category
        "8"              # Exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("main.load_from_file", return_value=recipe_book), \
         patch("main.print_menu"), \
         patch("main.save_to_file"), \
         patch("main.add_recipe") as mock_add:
        
        main()

        # Validate that add_recipe was called with the correct arguments
        mock_add.assert_called_once()
        args = mock_add.call_args[0]
        assert args[0] == recipe_book
        assert args[1] == "Pasta"
        assert args[2] == ["noodles", "tomato"]
        assert args[3] == "Boil and mix"
        assert args[4] == "Dinner"