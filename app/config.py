from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
from dotenv import load_dotenv
import torch
import os

# 🔥 Carregar variáveis do .env
load_dotenv()

# Configurações básicas
MODEL_ID = os.getenv("MODEL_ID", None)
HF_TOKEN = os.getenv("HF_TOKEN", None)

if not MODEL_ID:
    raise ValueError("❌ Variável MODEL_ID não encontrada. Verifique o arquivo .env.")

print(f"Carregando modelo {MODEL_ID}...")

# Login no Hugging Face
if HF_TOKEN:
    login(HF_TOKEN)
else:
    print("⚠️ Nenhum HF_TOKEN encontrado. Modelos privados não poderão ser carregados.")

# Carregar modelo e tokenizer (feito uma vez só)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

print("✅ Modelo carregado com sucesso")
