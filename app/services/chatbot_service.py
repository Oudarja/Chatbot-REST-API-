# app/services/chatbot_service.py
from app.utils.groq_client import generate_response
from app.services.product_service import get_product_by_name ,fetch_products
import json

def parse_user_message(message: str):
    """Return filter criteria or None"""
    message = message.lower()
    criteria = {}

    # Ratings
    if "rating" in message or "ratings" in message:
        import re
        match = re.search(r"above (\d+)", message)
        if match:
            criteria["min_rating"] = float(match.group(1))

    # Category
    categories = ["electronics", "beauty", "furniture", "clothing", "food",
    "fruit", "grocery", "home", "garden", "toys", "sports", "automotive",
    "groceries", "home decoration", "lighting",
    "men's clothing", "motorcycle", "skincare", "smartphones",
    "tops", "women's bags", "women's clothing", "women's shoes", "women's watches"]

    for cat in categories:
        if cat in message:
            criteria["category"] = cat

    return criteria if criteria else None


async def filter_products(criteria):
    products = await fetch_products()
    results = []

    for p in products:
        if "min_rating" in criteria and p["rating"] < criteria["min_rating"]:
            continue
        if "category" in criteria and p["category"].lower() != criteria["category"]:
            continue
        results.append(p)

    return results


async def get_chat_response(user_message: str) -> str:
    criteria = parse_user_message(user_message)
    
    if criteria:
        filtered_products = await filter_products(criteria)
        if filtered_products:
            products_json = json.dumps(filtered_products, indent=2)
            prompt = (
                f"You are a helpful assistant for an online store.\n"
                f"User asked: {user_message}\n"
                f"Here are the relevant products:\n{products_json}\n"
                "Answer in a natural, human-like way summarizing the product titles, prices, ratings, and other key info."
            )
        else:
            prompt = f"You are a helpful assistant. User asked: {user_message}. No products match the criteria."
    else:
        # fallback to single product search
        product = await get_product_by_name(user_message)
        if product:
            product_json = json.dumps(product, indent=2)
            prompt = (
                f"You are a helpful assistant for an online store.\n"
                f"User asked: {user_message}\n"
                f"Here is the product info:\n{product_json}\n"
                "Answer naturally including price, rating, shipping, and warranty."
            )
        else:
            prompt = f"You are a helpful assistant. User asked: {user_message}. Product not found."

    response = await generate_response(prompt)
    return response
