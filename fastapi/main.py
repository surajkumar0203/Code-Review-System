from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import httpx
import json
app = FastAPI()


class gitRepository(BaseModel):
    url:str
    pr_number:int
    git_token:Optional[str] = None

@app.post("/start_task/")
async def start_task_endpoint(task:gitRepository):
    data = {
        "url": task.url,
        "pr_number": task.pr_number,
        "git_token": task.git_token
    }
    
    url = "http://127.0.0.1:8002/api/task/"  # Django API endpoint
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, data=data)
            response.raise_for_status()  # Raise exception for HTTP errors
            response_data = response.json()  # Ensure response is JSON
            return {"task_id": response_data.get('id'), "status": response_data.get('status')}
    except httpx.HTTPStatusError as e:
        return {"error": "HTTP error occurred", "details": str(e)}
    except ValueError:  # If response is not JSON
            return {"error": "Invalid response from server", "details": response.text}
    

@app.get("/show_task/{task_id}/")
async def show_task_endpoint(task_id: str):
    url = f"http://127.0.0.1:8002/api/task/{task_id}/"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()  
    except httpx.HTTPStatusError as e:
            return {"error": "HTTP error occurred", "details": str(e)}
    except ValueError:  # If response is not JSON
        return {"error": "Invalid response from server", "details": response.text}