# 🍛 Namaste Bites AI Agent

Welcome to the **Namaste Bites AI Agent**! This is a specialized AI-powered receptionist for an Indian-style cafe, designed to handle food orders, table reservations, and customer inquiries using Google Gemini and LangGraph.

## 🚀 Features

- **Menu Exploration**: Get the latest menu with descriptions and prices.
- **Stock Tracking**: Check real-time availability of menu items.
- **Order Management**: Seamlessly place food orders.
- **Table Reservations**: Book a table for any party size and time.
- **Conversational AI**: Friendly and professional interaction powered by Gemini.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.10 or higher**
- **pip** (Python package manager)
- **Google AI API Key** (for Gemini)

---

## 💻 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Prabesh666/Cafe-AGENTS.git
cd Cafe-AGENTS/cafe-agent
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required libraries:
```bash
pip install fastapi uvicorn langchain-google-genai langgraph python-dotenv pydantic
```

---

## ⚙️ Configuration

Create a `.env` file in the `cafe-agent` directory (one is provided in the repository, but ensure it has your correct keys):

```env
GOOGLE_API_KEY="your_google_api_key_here"
FASTAPI_PORT=8000
```

---

## 🏃 Running the Project

To start the FastAPI server, run:

```bash
python main.py
```

The server will start at `http://localhost:8000`.

### API Endpoints

- **GET `/`**: Returns a welcome message.
- **POST `/chat`**: Send a message to the AI agent.
  - **Payload**: `{"message": "Can I see the menu?", "user_id": "optional_id"}`

---

## 📂 Project Structure

- `main.py`: The entry point for the FastAPI application.
- `tools.py`: Contains the logic for cafe operations (menu, orders, reservations).
- `db.py`: Handles data persistence for the menu and orders.
- `data/`: Directory where menu, inventory, and order JSON files are stored.

---

## 🎨 Design Persona
The agent acts as a receptionist for **Namaste Bites**, located at *123 Spice Lane, Foodtown*. It follows a professional yet warm tone, suitable for a premium dining experience.