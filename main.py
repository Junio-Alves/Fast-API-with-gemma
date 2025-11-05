from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login

# Carregar modelo e tokenizer
model_id = "google/gemma-3-1b-it"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

# Pergunta
input_text = "Quem foi Albert Einstein?"

# Tokenizar
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

# Gerar texto com parâmetros de controle
outputs = model.generate(
    **inputs,
    max_new_tokens=50,          # limite de tokens gerados
    do_sample=False,            # desativa aleatoriedade (respostas mais estáveis)
    eos_token_id=tokenizer.eos_token_id,  # para parar ao encontrar token <eos>
)

# Decodificar e exibir
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
