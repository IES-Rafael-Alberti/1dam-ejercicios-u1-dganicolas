contraseña = input("introduce la contraseña: ")
contaseñas = ('hola','admin','contraseña')

while contraseña not in contaseñas :
    contraseña = input("introduce la contraseña correcta: ")
    if contraseña in contaseñas:
        break
print("felicidades sabes la contraseña")