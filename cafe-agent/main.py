from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from tools import CAFE_TOOLS

# Load environment variables
load_dotenv()

app = FastAPI(title="Indian Cafe AI Agent API")

# Add CORS so our local webpage can talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Gemini
# Ensure you have GOOGLE_API_KEY set in your .env file
try:
    llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)
    llm_with_tools = llm.bind_tools(CAFE_TOOLS)
except Exception as e:
    print(f"Failed to initialize Gemini: {e}")
    llm = None
    llm_with_tools = None


class ChatRequest(BaseModel):
    message: str
    user_id: str = "default_user"

class ChatResponse(BaseModel):
    response: str


# System prompt that defines the agent's persona
CAFE_SYSTEM_PROMPT = """
You are a friendly, helpful, and professional AI Assistant for "Namaste Bites", an Indian-style cafe.
Your role includes taking food orders, making table reservations, and answering questions about the menu, hours, and location.
You should always be polite and use conversational language suitable for a cafe receptionist.

Our hours are:
Monday-Friday: 8:00 AM - 10:00 PM
Saturday-Sunday: 9:00 AM - 11:00 PM

Our location is: 123 Spice Lane, Foodtown.

Currently we have a limited interaction scope, but please be welcoming!
"""


@app.get("/")
async def root():
    return {"message": "Welcome to the Indian Cafe AI Agent API"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not llm_with_tools:
        return {"response": "I'm sorry, my brain is currently offline (API Key issue)."}
    
    # Create the agent
    agent = create_react_agent(llm, CAFE_TOOLS, prompt=CAFE_SYSTEM_PROMPT)

    try:
        # Invoke the agent with the user's message
        inputs = {"messages": [("user", request.message)]}
        result = agent.invoke(inputs)
        
        # The output messages contain the reasoning and final response.
        # The last message is the AI's final answer to the user.
        final_response = result["messages"][-1].content
        
        # Handle cases where content is a list of blocks (e.g. Gemini 3)
        if isinstance(final_response, list):
            final_response = " ".join(
                block["text"] for block in final_response if block.get("type") == "text"
            )
        
        return {"response": str(final_response)}
    except Exception as e:
         return {"response": f"Sorry, I encountered an error computing that: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
