from fastapi import FastAPI
from app.resources.ai import ai_resource 
from app.resources.links import link_resource
from fastapi.middleware.cors import CORSMiddleware
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')

app = FastAPI(title="auto-publisher-backend", version="0.1.0", root_path="/api/v1")
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
app.include_router(link_resource.router)