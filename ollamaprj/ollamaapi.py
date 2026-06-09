from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from typing import List

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Ollama model
llm = ChatOllama(
    model="deepseek-r1:1.5b",
    base_url="http://localhost:11434",
    temperature=0.7
)

# Store conversation history (in production, use a database or session storage)
conversation_history = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"  # Optional session ID for multiple conversations

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Get or create conversation history for this session
        if request.session_id not in conversation_history:
            conversation_history[request.session_id] = []
        
        history = conversation_history[request.session_id]
        
        # Add user message to history
        history.append(HumanMessage(content=request.message))
        
        # Prepare the prompt with history
        messages = [
            SystemMessage(content="You are a helpful chatbot powered by DeepSeek-R1. Provide clear and concise answers.")
        ] + history
        
        # Create the formatted prompt
        formatted_prompt = ChatPromptTemplate.from_messages(messages)
        
        # Create the chain
        chain = formatted_prompt | llm
        
        # Invoke the model
        response = chain.invoke({"user_input": request.message})
        response_text = response.content
        
        # Add model response to history
        history.append(AIMessage(content=response_text))
        
        # Update conversation history
        conversation_history[request.session_id] = history
        
        return ChatResponse(response=response_text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@app.delete("/chat/{session_id}")
async def clear_chat_history(session_id: str):
    """Clear conversation history for a specific session"""
    if session_id in conversation_history:
        del conversation_history[session_id]
        return {"message": f"Chat history cleared for session {session_id}"}
    return {"message": f"No history found for session {session_id}"}

@app.get("/chat/{session_id}/history")
async def get_chat_history(session_id: str):
    """Get conversation history for a specific session"""
    if session_id in conversation_history:
        # Convert messages to a readable format
        history = []
        for msg in conversation_history[session_id]:
            if isinstance(msg, HumanMessage):
                history.append({"type": "human", "content": msg.content})
            elif isinstance(msg, AIMessage):
                history.append({"type": "ai", "content": msg.content})
        return {"history": history}
    return {"history": []}

if __name__ == "__main__":
    print("Starting Fire.ai Server powered by DeepSeek-R1...")
    print("Server will be available at http://localhost:8000")
    print("API Documentation at http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)