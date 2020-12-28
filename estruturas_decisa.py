idade = 20

if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")


veiculo = {"tipo": "moto", "marca": "honda", "potencia_motor": 140}


if veiculo["tipo"] == "moto" and veiculo["marca"] == "honda":
    print("o veiculo é uma moto")
else:
    print("O veiculo não é uma moto")


resultado = veiculo["tipo"] == "moto"

print(resultado)

if veiculo["tipo"] == "moto" or veiculo["porencia_motor"] > 100:
    print("o veiculo é muito rapido")
