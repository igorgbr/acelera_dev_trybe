lista_convidados = ["Sara", "Julio", "Rangel", "Kaecio"]

print(lista_convidados)

lista_convidados.append("Fabiola")

print(lista_convidados)

lista_convidados.remove("Rangel")

print(lista_convidados)

print(lista_convidados[0])

print(lista_convidados[-1])

lista_convidados.append(30)

print(lista_convidados)

# tupla
tupla1 = (1, 2, 3)

print(tupla1)

tupla2 = (4, 5, 6)

print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)


# chave -> valor
dados_pessoais = {"nome": "Batman", "cidade": "Gothan"}

print(dados_pessoais)

dados_pessoais["veiculo"] = "Batmovel"

print(dados_pessoais)

del dados_pessoais['cidade']

print(dados_pessoais)
