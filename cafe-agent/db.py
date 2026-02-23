import json
import os
from pathlib import Path
from typing import Dict, Any, List

DATA_DIR = Path(__file__).parent / "data"

MENU_FILE = DATA_DIR / "menu" / "menu.json"
INVENTORY_FILE = DATA_DIR / "inventory" / "inventory.json"
ORDERS_DIR = DATA_DIR / "orders"
RESERVATIONS_DIR = DATA_DIR / "reservations"

def init_db():
    """Initializes the data directories and default JSON files if they don't exist."""
    print(f"Initializing data at {DATA_DIR}...")
    
    # Ensure all directories exist
    MENU_FILE.parent.mkdir(parents=True, exist_ok=True)
    INVENTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    ORDERS_DIR.mkdir(parents=True, exist_ok=True)
    RESERVATIONS_DIR.mkdir(parents=True, exist_ok=True)

    # Create default menu if it doesn't exist
    if not MENU_FILE.exists():
        default_menu = [
            {"id": "samosa", "name": "Samosa", "price": 4.50, "description": "Crispy pastry filled with spiced potatoes and peas.", "tags": ["vegan", "snack"]},
            {"id": "butter_chicken", "name": "Butter Chicken", "price": 16.00, "description": "Tender chicken cooked in a rich and creamy tomato sauce.", "tags": ["main", "non-veg"]},
            {"id": "paneer_tikka", "name": "Paneer Tikka Masala", "price": 14.50, "description": "Grilled paneer cheese in a spiced gravy.", "tags": ["vegetarian", "main", "gluten-free"]},
            {"id": "naan", "name": "Garlic Naan", "price": 3.00, "description": "Soft flatbread topped with garlic and cilantro.", "tags": ["vegetarian", "bread"]},
            {"id": "mango_lassi", "name": "Mango Lassi", "price": 5.00, "description": "Sweet yogurt drink blended with ripe mangoes.", "tags": ["vegetarian", "drink", "cold"]}
        ]
        with open(MENU_FILE, 'w') as f:
            json.dump(default_menu, f, indent=4)
        print("Created default menu.json")

    # Create default inventory if it doesn't exist
    if not INVENTORY_FILE.exists():
        default_inventory = {
            "samosa": {"stock": 50, "unit": "pieces"},
            "butter_chicken": {"stock": 30, "unit": "servings"},
            "paneer_tikka": {"stock": 25, "unit": "servings"},
            "naan": {"stock": 100, "unit": "pieces"},
            "mango_lassi": {"stock": 40, "unit": "glasses"}
        }
        with open(INVENTORY_FILE, 'w') as f:
            json.dump(default_inventory, f, indent=4)
        print("Created default inventory.json")


def load_menu() -> List[Dict[str, Any]]:
    with open(MENU_FILE, 'r') as f:
        return json.load(f)

def load_inventory() -> Dict[str, Any]:
    with open(INVENTORY_FILE, 'r') as f:
        return json.load(f)

# Initialize when the module is imported
init_db()
