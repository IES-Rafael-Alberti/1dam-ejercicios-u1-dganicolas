numero = int(input("dame un numero positivo: "))
while numero < 0:
    numero = int(input("dame un numero positivo: "))
cont = numero
serie = "serie => " + str(numero)
while cont > 0:
    cont-=1
    serie = serie + "," + str(cont)
print(serie)