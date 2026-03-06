# 🍛 Namaste Bites AI Agent

Welcome to the **Namaste Bites AI Agent**! This is a beginner-friendly, AI-powered receptionist for an Indian-style cafe. It uses Google Gemini and LangGraph to talk to customers, take food orders, check if items are in stock, and book tables.

---

## ✨ Features

- **Conversational AI**: Friendly and professional interaction powered by Gemini.
- **Menu Exploration**: Ask the AI for the latest menu and prices.
- **Stock Tracking**: The AI checks real-time availability of menu items.
- **Order Management**: Seamlessly place food orders by chatting.
- **Table Reservations**: Book a table for any party size and time.

---

## � Quick Start Guide

Follow these simple steps to get the AI agent running on your computer.

### Step 1: Clone the Repository
Download the code to your computer:
```bash
git clone https://github.com/Prabesh666/Cafe-AGENTS.git
cd Cafe-AGENTS
```

### Step 2: Install Requirements
It's recommended to use a virtual environment, but the main goal is to install the required Python packages. Run this command:
```bash
pip install -r requirements.txt
```
*(If you use a virtual environment, create and activate it first with `python3 -m venv venv` and `source venv/bin/activate` or `venv\Scripts\activate` on Windows)*

### Step 3: Add Your API Key
The AI needs a Google Gemini API key to think and talk. 
1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Inside the `cafe-agent` folder, create a new file named `.env`.
3. Add your key to the `.env` file like this:
```env
GOOGLE_API_KEY="your_google_api_key_here"
```

### Step 4: Run the Server
Start the FastAPI server using `uvicorn`:
```bash
cd cafe-agent
uvicorn main:app --reload
```
🎉 **That's it!** Your AI Cafe server is now running at `http://127.0.0.1:8000`.

---

## 💬 How to Talk to the AI

You can test the AI by sending a request to the chat endpoint. Open a new terminal and run:

```bash
curl -X POST http://127.0.0.1:8000/chat \
-H "Content-Type: application/json" \
-d '{"message": "Hi! Can I see the vegetarian menu?"}'
```

The AI will respond with the menu options!

---

## ☁️ Deploying to Vercel

This project is deployment-ready for **Vercel** serverless functions! It includes a `vercel.json` file.
Just push your code to GitHub, import the repository in Vercel, and add your `GOOGLE_API_KEY` in the Vercel Environment Variables settings.

*(Note: Data is saved to the temporary `/tmp` folder on Vercel, meaning orders and reservations will reset when the server restarts. For a production app, connect a real database.)*

---

## 📂 Project Structure

- `requirements.txt`: List of Python packages needed to run the app.
- `vercel.json`: Configuration for deploying to Vercel.
- `cafe-agent/`
  - `main.py`: The FastAPI application and AI Agent core logic.
  - `tools.py`: Tools the AI uses to check the menu, make orders, and reserve tables.
  - `db.py`: Simple database logic to save orders and reservations.
  - `data/`: Local folder where JSON files for menu, inventory, and orders are stored.