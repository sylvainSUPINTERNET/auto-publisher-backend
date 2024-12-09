from fastapi import APIRouter
from fastapi.responses import JSONResponse
from infrastructure.rabbitmq_conn import RabbitMqClient

router = APIRouter()


## TODO: move this into consummer
@router.get("/wait")
async def clipping():

    rabbitmq_client = RabbitMqClient()

    rabbitmq_client.get_conn().channel().basic_publish(exchange='', routing_key='yt_dl_queue', body='{"url": "https://www.youtube.com/watch?v=6v2L2UGZJAM"}')
    
    return JSONResponse(content={"message": "Hello World"}, status_code=200)