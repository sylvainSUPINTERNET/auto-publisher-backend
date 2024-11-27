from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/ai")
async def clipping():

    # TODO : transcribe ( whisper ) 
    # TODO : use prompt with chatgpt
    # Add text to the frame ( using pymovie ) 
    
    return JSONResponse(content={"message": "Hello World"}, status_code=200)