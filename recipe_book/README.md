# 🥘 RecipeBook CLI App

A command-line application for managing your personal recipe collection.

Features:
- Add and delete recipes
- Filter recipes by category
- Prevents duplicate entries
- JSON-based data persistence

### 🚧 Work In Progress
This project is still in active development. Upcoming features may include:
- Recipe search improvements
- Editable recipe entries
- Unit tests
- UI/UX enhancements

### 💡 Tech Stack
- Python 3
- JSON for data storage
- Virtualenv for dependency management

---

Built as part of a Python refresh journey.

```bash
recipe_book/
├── main.py                # Runs the CLI app
├── models.py              # Recipe, RecipeBook classes
├── storage.py             # JSON saving/loading logic
├── utils.py               # CLI helper functions
├── requirements.txt       # For dependencies (optional)
├── README.md              # Project overview
└── data/
    └── recipes.json       # Data store (can be empty at first)