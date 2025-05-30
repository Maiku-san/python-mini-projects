# 🥘 RecipeBook CLI App

A command-line application for managing your personal recipe collection.

Features:
- Add and delete recipes
- Filter recipes by category
- Prevents duplicate entries
- JSON-based data persistence

### 🚧✅ Mini Project Status
This project was built as a Python practice exercise. It implements a basic recipe book with features like adding, listing, editing, deleting, and filtering recipes. While there are many possible improvements, the current version can serve as a foundation for future enhancements or refactoring.

Feel free to explore!

### 💡 Tech Stack
- Python 3
- JSON for data storage
- Virtualenv for dependency management

---

Built as part of a Python refresh journey.

```bash
recipe_book/
├── data/
│   └── recipes.json       # Data store (can be empty at first)
├── tests/                 # Test cases will go here
│   └── test_main.py       
│   └── test_utils.py      
├── main.py                # Runs the CLI app
├── models.py              # Recipe, RecipeBook classes
├── pytest.ini             # Tests config file
├── README.md              # Project overview
├── requirements.txt       # For dependencies (optional)
├── storage.py             # JSON saving/loading logic
└── utils.py               # CLI helper functions
