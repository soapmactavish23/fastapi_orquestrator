from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

from src.drivers.ollama_client import OllamaClient
from src.prompts.prompt_programmer import PYTHON_EXPERT_PROMPT

generate_router = APIRouter()

class PromptRequest(BaseModel):
    user_prompt: str

@generate_router.post("/prompt")
async def enrich_and_generate_response(request: PromptRequest):
    try:
        enriched_prompt = PYTHON_EXPERT_PROMPT.format(user_prompt=request.user_prompt)
        ollama_client = OllamaClient()

        response = await ollama_client.generate(enriched_prompt)
        llm_response = response["message"]["content"]

        return JSONResponse(status_code=200, content={"response", llm_response})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})