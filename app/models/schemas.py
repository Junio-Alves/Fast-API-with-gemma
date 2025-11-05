from pydantic import BaseModel

class GenerateRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 100
    do_sample: bool = False

class GenerateResponse(BaseModel):
    response: str
