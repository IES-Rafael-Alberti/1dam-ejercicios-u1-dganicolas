amount= int(input("cantidad a invertir: "))
interest= float(input("Interes porcentual anual: "))
años= int(input("cuantos años: "))
cont= 0
año= 1
while años > cont:
    amount *= 1 + interest / 100
    print("el año " + str(año) + " has conseguido esto " + str(round(amount,2)))
    cont +=1
    año +=1