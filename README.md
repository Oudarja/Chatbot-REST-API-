# Chatbot REST API with FastAPI and Groq LLM

This project is a **Chatbot REST API** built using **FastAPI**. It interacts with customers and provides **human-like answers about product details** using data from the [DummyJSON Products API](https://dummyjson.com/products). The chatbot uses **Groq LLM** for generating responses and supports **RAG-style reasoning** for context-aware answers.

---

## Features

- Fetch all products from DummyJSON API.
- Search products by title (supports **fuzzy matching**).
- Filter products by category, rating, and other attributes.
- Generate natural, human-like responses using **Groq LLM**.
- Fully async FastAPI implementation.
- Modular project structure for easy maintenance.

---
## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Oudarja/Chatbot-REST-API-.git
cd Chatbot-REST-API

```
### Create Virtual env
#### python version:3.9
```

python -m venv .venv
source .venv/bin/activate    # Linux / Mac
.venv\Scripts\activate       # Windows
```

### Install all dependencies
```
pip install -r requirements.txt
```

### Environment Variables
#### Create a .env file in the root directory and add:
```
GROQ_API_KEY=your_groq_api_key
GROQ_LLM_MODEL=llama-3.3-70b-versatile
DUMMYJSON_URL=https://dummyjson.com/products
```
### Run the app
```
uvicorn app.main:app --reload
```
### Image
- Fetch all products
  
  <img width="1240" height="867" alt="image" src="https://github.com/user-attachments/assets/9e4c1c96-8068-4c7c-a713-1548b604056f" />
  
- LLM Response on user message
  
  <img width="1197" height="818" alt="image" src="https://github.com/user-attachments/assets/04bbf924-2c26-40a9-b930-0a8c20e18236" />
  
  <img width="1168" height="825" alt="image" src="https://github.com/user-attachments/assets/b336e3c7-26d9-48eb-b0c1-c7d9fdfece4b" />





