# app/api/routes_chatbot.py
from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chatbot_service import get_chat_response
from app.services.product_service import fetch_products

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    '''
    Handle chat requests and return LLM responses
    '''
    resp = await get_chat_response(req.message)
    return {"response": resp}

@router.get("/products")
async def get_all_products():
    """
    Fetch and return all products from DummyJSON API
    """
    products = await fetch_products()
    return {"products": products}
