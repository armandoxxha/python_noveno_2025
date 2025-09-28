# Reto 1: Crea un bucle, usando un ciclo for, imprima tu nombre 5 veces.
# usando un ciclo for con range()  que permita definir el número de veces que se repite el bucle.

for i in range(1,6):
    print("Imprimiendo mi nombre: Armando")

# Reto 2: Crea un bucle que imprima los números del 1 al 20.
# usando un ciclo for con range()  que permita definir el número de veces que se repite el bucle.

for i in range(1, 21):
    print("El numero es: ", i)

# Reto 3: Crea un bucle que imprima todos los números pares entre 1 y 50. Usar la función % módulo.
# usando un ciclo for con range()  que permita definir el número de veces que se repite el bucle.
# Usando el operador módulo (%) para determinar si un número es par.
# usando un condicional if - else para determinar si el número es par o impar.

for i in range(1, 51):
    if i % 2 == 0:
        print("El numero es par:", i)
    else:
        print("El numero es impar:", i)

# Reto 4: Escribe un programa que pida al usuario que ingrese una contraseña. El programa debe seguir pidiendo la contraseña mientras no 
# sea 'secreto'. Usar bucle while.

# Usando un bucle while para repetir la solicitud de contraseña hasta que se ingrese la correcta.
# Definiendo la contraseña correcta como 'secreto'.
# Usando un condicional if - else para verificar si la contraseña es correcta o no. 
# Si es correcta, imprimir un mensaje de bienvenida. Si no, imprimir un mensaje de error e intentar de nuevo.

contBase = "prueba1234"
contraseIngresada = ""

while contraseIngresada != contBase:
    contraseIngresada = input("Ingrese la contraseña: ")
    if contraseIngresada == contBase:
        print("Contraseña correcta! Bienvenido!")
    else:
        print("Contraseña incorrecta! Intente de nuevo.")


# Reto 5: 
# "Imagina que eres un cajero automático
# muy simple. Crea un programa que use un 
# ciclo while para preguntar al usuario 
# “¿Quieres hacer otra transacción? (Si/No)”.
#  El programa debe de seguir preguntando 
# mientras el usuario escribe “Si”. Cuando 
# el usuario escriba “No”, el programa debe
# decir “Gracias por usar nuestros servicios”.

decision = "si"
while decision == "si":
  print(":::Cajero Automático:::")
  print("1- Retirar")
  print("2- Depositar")
  opcion = int(input("Seleccione una opción: "))
  if opcion == 1:
    dinero = int(input("Monto a retirar: "))
    print("Monto retirado: ", dinero)
  elif opcion == 2:
    dinero = int(input("Monto a depositar: "))
    print("Monto depositado: ", dinero)
  else:
    print("Opción incorrecta")

  decision = input("Deseas realizar una transaccion. (SI/NO): ").lower()
print("¡Gracias! por usar nuestros servicios") 
