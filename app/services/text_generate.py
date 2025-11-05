from app.config import tokenizer, model
import torch

def generate_text(prompt: str, max_new_tokens: int = 100, do_sample: bool = False) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        eos_token_id=tokenizer.eos_token_id,
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
