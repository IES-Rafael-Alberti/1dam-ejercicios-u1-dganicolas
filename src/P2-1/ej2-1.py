edad = int(input("introduce tu edad: "))
while edad < 0:
    print("ERROR, los numero negativos no son edades")
    edad = int(input("introduce tu edad: "))
if 18 <= edad:
    print("felicidades eres mayor de edad")
elif 18 > edad:
    print("felicidades eres menor de edad")