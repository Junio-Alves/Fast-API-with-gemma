from fastapi import FastAPI
from app.models.schemas import GenerateRequest, GenerateResponse
from app.services.text_generate import generate_text

app = FastAPI(title="Gemma API (Arquitetura simples)")

@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    result = generate_text(
        prompt=request.prompt,
        max_new_tokens=request.max_new_tokens,
        do_sample=request.do_sample
    )
    return {"response": result}


@app.get("/")
async def root():
    """Simple root endpoint for health check / basic info."""
    return {"status": "ok", "message": "Gemma API running"}
