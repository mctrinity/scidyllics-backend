from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Use the new OpenAI Client (Correct for v1.0.0+)
client = openai.OpenAI(api_key=api_key)

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat/")
async def chat(request: ChatRequest):
    try:
        print(f"📝 Received message: {request.message}")  # Debugging

        # ✅ Use the new OpenAI API format
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}],
        )

        # ✅ Extract response correctly
        reply_message = response.choices[0].message.content

        print(f"✅ OpenAI Response: {reply_message}")  # Debugging
        return {"reply": reply_message}

    except Exception as e:
        print(f"❌ Error calling OpenAI: {e}")  # Debugging
        raise HTTPException(status_code=500, detail=str(e))
