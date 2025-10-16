# app/services/product_service.py
import os
import httpx
from difflib import get_close_matches

DUMMYJSON_URL = os.getenv("DUMMYJSON_URL")

async def fetch_products():
    async with httpx.AsyncClient() as client:
        resp = await client.get(DUMMYJSON_URL)
        resp.raise_for_status()
        data = resp.json()
        return data.get("products", [])


async def get_product_by_name(name: str):
    products = await fetch_products()
    name_lower = name.lower()
    
    # Direct title match . search for any title match 
    for p in products:
        if name_lower in p["title"].lower():
            return p
    
    # Search tags
    for p in products:
        if any(name_lower in tag.lower() for tag in p.get("tags", [])):
            return p
    
    # Search description
    for p in products:
        if name_lower in p.get("description", "").lower():
            return p
    
    # Fuzzy title match
    titles = [p["title"] for p in products]
    match = get_close_matches(name, titles, n=1, cutoff=0.6)
    if match:
        for p in products:
            if p["title"] == match[0]:
                return p

    return None
