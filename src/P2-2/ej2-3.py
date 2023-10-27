numero = int(input("dame un numero positivo"))
while numero < 0:
    numero = int(input("dame un numero positivo"))
cont = 0
serie = "impar => "
num = 1
while cont < numero:
    divisor = num%2
    if divisor == 1:
        serie= serie + "," + str(num)
    cont+=1
    num+=1
print(serie)