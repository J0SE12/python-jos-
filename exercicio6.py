import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

senha = gerar_senha(8)
print(senha)  # exemplo de saída: "YdGm$p0gH~o&"

