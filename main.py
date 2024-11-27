from fastapi import FastAPI
from app.resources.ai import ai_resource 
from fastapi.middleware.cors import CORSMiddleware
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')

app = FastAPI(title="auto-publisher-backend", version="0.1.0")
origins = [
    "*",  # Allows requests from any origin (use with caution in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register your routes
app.include_router(ai_resource.router)