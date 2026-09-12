import json

with open("data/base_conhecimento.json", "r", encoding="utf-8") as f:
    base = json.load(f)

pergunta = input("Digite sua dúvida: ").lower()

encontrado = False
for item in base:
    for palavra in item["palavras_chave"]:
        if palavra in pergunta:
            print(item["solucao"])
            encontrado = True
            break

if not encontrado:
    print("Não encontrei essa informação na base de conhecimento.")
