from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.resources.ai import ai_resource 
from app.resources.links import link_resource
from fastapi.middleware.cors import CORSMiddleware
import logging
from dotenv import load_dotenv
import os
import pika

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')


rabbitmq_connection = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # rabbitmq_connection = pika.BlockingConnection(pika.URLParameters(f"{os.getenv('RABBIT_MQ_URL', '')}"))
        # ch1  = rabbitmq_connection.channel()
        # ch1.queue_declare(queue='hello')
        # ch1.basic_publish(exchange='', routing_key='hello', body='Hello LLLLAAA!')

        logging.info(f"Starting the application")
        yield
    finally:
        logging.info("Shutting down the application")

app = FastAPI(title="auto-publisher-backend", version="0.1.0", root_path="/api/v1", lifespan=lifespan)

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


