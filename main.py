#executar comando abaixo para adicionar a openai no projeto
#pip install openai

import json
from openai import OpenAI

# API KEY 
client = OpenAI(api_key="CHAVE_API_OPENAI")

# dados inicias e arquivo json
with open("entrada.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

resultado = []
#loop nos clientes
for cliente in dados:
    print("Gerando mensagem para:", cliente["nome"])

    # mensagem para enviar a IA
    prompt = f"""
    Crie uma mensagem publicitária para este cliente:

    Nome: {cliente['nome']}
    Idade: {cliente['idade']}
    Saldo: {cliente['saldo']}
    Perfil: {cliente['perfil']}

    Seja direto, amigável e personalizado.
    """

    # chamada da IA
    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    mensagem = resposta.choices[0].message.content

    # retorno da IA
    resultado.append({
        "nome": cliente["nome"],
        "email": cliente["email"],
        "mensagem": mensagem
    })

# salva resultado em novo arquivo json
with open("resultado.json", "w", encoding="utf-8") as arquivo:
    json.dump(resultado, arquivo, indent=4, ensure_ascii=False)

print("Pronto! Arquivo resultado.json gerado.")
