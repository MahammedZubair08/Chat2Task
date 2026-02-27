from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.parser import parse_command
from app.services.executor import execute_command

router = APIRouter()

class CommandRequest(BaseModel):
    message: str
    sender: str

@router.post("/process-command")
def process_command(request: CommandRequest):
    try:
        parsed_data = parse_command(request.message)
        result = execute_command(parsed_data)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))