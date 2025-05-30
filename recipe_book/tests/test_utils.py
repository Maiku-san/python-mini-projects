import pytest
from utils import add_recipe
from models import RecipeBook, Recipe


# Setup a temporary recipe book for testing
@pytest.fixture
def recipe_book():
    # Create a new RecipeBook object for testing
    return RecipeBook()

# Fixture to create a sample recipe to reuse across tests
@pytest.fixture
def sample_recipe():
    return Recipe(
        title="Toast",
        ingredients=["Bread", "Butter"],
        instructions="Toast the bread.",
        category="Breakfast"
    )


def test_add_recipe_success(recipe_book, sample_recipe):
    # Act
    success = add_recipe(
        recipe_book,
        sample_recipe.title,
        sample_recipe.ingredients,
        sample_recipe.instructions,
        sample_recipe.category
    )
    
    # Assert
    assert success is True
    assert len(recipe_book.recipes) == 1
    assert recipe_book.recipes[0].title == sample_recipe.title
    assert recipe_book.recipes[0].category == sample_recipe.category


# Test for adding a duplicate recipe (using the fixture)
def test_add_recipe_failure_due_to_duplicate(recipe_book, sample_recipe):
    # Arrange (add the first recipe)
    add_recipe(recipe_book, sample_recipe.title, sample_recipe.ingredients, sample_recipe.instructions, sample_recipe.category)
    
    # Act (try to add the same recipe again)
    success = add_recipe(recipe_book, sample_recipe.title, sample_recipe.ingredients, sample_recipe.instructions, sample_recipe.category)
    
    # Assert (should fail, no duplicate added)
    assert success is False
    assert len(recipe_book.recipes) == 1  # Only one recipe should exist