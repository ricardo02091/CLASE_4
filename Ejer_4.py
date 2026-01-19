#Validador de Password

password = input("Digite un password: ")

#verificar (len, significa que me lea la variable)
#"longitud_ok" la contraseña debe ser igual o mas de 8 caracteres
#que "no_password" no sea la palabra "password"
#y que "no_mun" no sean los numeros en orden "12345678"
longitud_ok = len(password) >= 8
no_password = password != "password"
no_num = password != "12345678"

#Los "and" me da la condicion que tengo que cumplir si o si todas las condiciones: 
password_valido = longitud_ok and no_password and no_num

print(f"Password valida: {password_valido}")