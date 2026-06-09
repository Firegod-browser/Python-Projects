from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Simple echo response - replace with your actual chat logic
        response_text = f"You said: {request.message}"
        
        # TODO: Replace this with your actual chat processing logic
        # For example:
        # response_text = your_chat_function(request.message)
        
        return ChatResponse(response=response_text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage, AIMessage


# Initialize the Ollama model
llm = ChatOllama(
    model="deepseek-r1:1.5b",
    base_url="http://localhost:11434",
    temperature=0.7
)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful chatbot powered by DeepSeek-R1. Provide clear and concise answers."),
    *[],  # Placeholder for conversation history
    HumanMessage(content="{{user_input}}")
])

# Initialize conversation history
history = []

def main():
    print("Welcome to Nikhil's Chatbot powered by DeepSeek-R1! Type 'exit' to quit.")
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        # Add user message to history
        history.append(HumanMessage(content=user_input))
        # Prepare the prompt with history
        messages = [
            SystemMessage(content="You are a helpful chatbot powered by DeepSeek-R1. Provide clear and concise answers.")
        ] + history
        # Update prompt with current messages
        formatted_prompt = ChatPromptTemplate.from_messages(messages)
        # Create the chain
        chain = formatted_prompt | llm
        # Invoke the model
        try:
            response = chain.invoke({"user_input": user_input})
            response_text = response.content
            # Add model response to history
            history.append(AIMessage(content=response_text))
            # Print response
            print(f"Bot: {response_text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()