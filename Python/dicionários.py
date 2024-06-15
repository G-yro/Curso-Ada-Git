dicionário = {}
dicionário = dict()

dicionário = { "Nome": "Gustavo", "Idade": "18 anos", "Altura": "1,80 m" }

print(dicionário)
print(dicionário["Altura"])
dicionário["Programador"] = True
print(dicionário)

dicionário["Altura"] = 2
print(dicionário)

for chave in dicionário:
    print(chave, dicionário[chave])

print("Peso" in dicionário)
print("Altura" in dicionário)