# Reto 1 
# 1: Imprime por consola tu nombre si una
# variable toma su valor. Usar condicional
# simple (if - else)
"""
nombre = "dennis"
if nombre == "dennis":
  print("Bienvenido! ", nombre)
else:
  print("El usuario no existe")
"""
#Reto 2: Imprime por consola un mensaje si 
#el usuario y contraseña coincide con unos
#establecidos. Usar condicional simple (if - else)
"""
nombre = "dennis"
password = "dennis123"
if nombre == "dennis" and password == "dennis123":
  print("Bienvenido! ", nombre)
else:
  print("El usuario no existe")
"""
# Reto 3: Verifica sin un número es positivo,
# negativo o cero e imprime un mensaje. Usar
# condicional anidada (if - elif - else)
"""
numero = int(input("Ingrese un número: "))
if numero > 0:
  print("El número: ", numero, " es positivo.")
elif numero < 0:
  print("El número: ", numero, " es negativo.")
else:
  print("El número es cero.")
"""

# Reto 4: Verifica si una persona puede votar o no
# (mayor o igual a 18) e indicia cuántos años
# le faltan si no reune la edad necesaria para
# votar. Usar condicional simple (if - else)
"""
edad = int(input("Ingrese su edad para votar: "))

if edad >= 18:
  print("Eres mayor de edad y puedes votar.")
else:
  print("Te faltan: ", 18 - edad, " años para votar.")

"""

# Reto 6: Realizar un programa que pueda 
#realizar una suma, una resta, una
# multiplicación o una división de dos 
# números enteros, dependiendo de la decisión 
#del usuario a la cual le
# vamos a llamar operación:
print("Calculadora: ")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")

op = int(input("Selecciona una opción: "))
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

if op == 1:
  print("La suma es igual: ", num1 + num2)
elif op == 2: 
  print("La resta es igual: ", num1 - num2)
elif op == 3: 
  print("La multi es igual: ", num1 * num2)
else: 
  print("La division es igual: ", num1 / num2)
