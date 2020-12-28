for i in range(10):
    print(i)

convidados = ["elvis", "marilyn", "johnatan", "picasso", "hitler", "luluzinha"]

for convidado in convidados:
    print(convidado + " esta convidado")

for i in range(len(convidados)):
    convidado = convidados[i]
    print(convidado + " esta convidado (for range)")

counter = 0

while counter < 5:
    counter = counter + 1
    print('contador: ' + str(counter))