from langchain.tools import tool
import json
import uuid
import os
from datetime import datetime
from db import load_menu, load_inventory, ORDERS_DIR, RESERVATIONS_DIR

@tool
def get_menu(category: str = None) -> str:
    """Gets the cafe menu. You can optionally pass a category like 'vegetarian', 'vegan', 'drink', or 'main'."""
    menu = load_menu()
    
    if category:
        filtered = [item for item in menu if category.lower() in [t.lower() for t in item.get('tags', [])]]
        if not filtered:
            return f"We don't have any items matching '{category}' right now."
        result = filtered
    else:
        result = menu
        
    formatted = "\n".join([f"- {item['name']} (${item['price']:.2f}): {item['description']}" for item in result])
    return formatted

@tool
def check_item_availability(item_id: str) -> str:
    """Checks if a specific menu item is in stock using its short ID (e.g. 'samosa' or 'butter_chicken')."""
    inventory = load_inventory()
    
    if item_id not in inventory:
        return f"Warning: I couldn't find an item with the ID '{item_id}' in our inventory system."
        
    in_stock = inventory[item_id]['stock']
    if in_stock > 0:
        return f"Yes, we have {in_stock} {inventory[item_id]['unit']} of {item_id} currently in stock."
    else:
        return f"Sorry, {item_id} is currently sold out."

@tool
def place_order(customer_name: str, item_ids: list[str]) -> str:
    """Places a new food order. Pass the customer name and a list of item short IDs."""
    
    # In a real app, we would decrement inventory here.
    order_id = str(uuid.uuid4())[:8]
    
    order = {
        "order_id": order_id,
        "status": "pending",
        "timestamp": datetime.now().isoformat(),
        "customer": customer_name,
        "items": item_ids
    }
    
    with open(ORDERS_DIR / f"{order_id}.json", 'w') as f:
        json.dump(order, f, indent=4)
        
    return f"Success! Order {order_id} has been placed for {customer_name}. The kitchen will be notified."

@tool
def make_reservation(customer_name: str, date_time: str, party_size: int) -> str:
    """Books a table reservation. Provide the customer name, the requested date/time (e.g., 'Tonight at 7PM'), and the number of people."""
    res_id = str(uuid.uuid4())[:8]
    
    reservation = {
        "reservation_id": res_id,
        "customer": customer_name,
        "date_time_requested": date_time,
        "party_size": party_size,
        "status": "confirmed"
    }
    
    with open(RESERVATIONS_DIR / f"{res_id}.json", 'w') as f:
        json.dump(reservation, f, indent=4)
        
    return f"Amazing. A reservation for {party_size} people has been confirmed for {customer_name} at {date_time}. Booking ID: {res_id}."

# Define tool list for the agent
CAFE_TOOLS = [get_menu, check_item_availability, place_order, make_reservation]
