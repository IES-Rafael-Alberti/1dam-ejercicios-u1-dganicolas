numero = int(input("dame un numero positivo: "))
while numero < 0:
    numero = int(input("dame un numero positivo: "))
serie = "*"
while numero > 0:
    print(serie)
    serie += "*"
    numero-= 1