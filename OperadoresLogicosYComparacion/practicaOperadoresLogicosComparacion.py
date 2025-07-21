# Operadores de asignación
print("Operadores De Asignación")
numero = 30
print(numero)
print("Operador de asignacion += ")
# operador de asignación +=
numero += 45
print(numero)

print("Operador de asignacion -= ")
# operador de asignación -=

numero -= 20
print(numero)

print("Operador de asignacion *= ")
# Operador de asignación *= 

numero *= 2
print(numero)

print("Operador de asignacion /= ")
# Operador de asignación /=

numero /= 3
print(numero)


# Operadores de comparación

# primero ">" Mayor que
print("Operadores Comparación >")
numA = 20
numB = 30

print(numA > numB)
print(89 > 45)
print(55 > 55)

# segundo "<" menor que
print("Operadores Comparación <")
print(numA < numB)
print(89 < 23)
print(100 < 100)

# tercero "==" igual que
print("Operadores Comparación ==")
print(numA == numB)
print("gato" == "Gato")
print(120 == 68)

# Cuarto "!=" Diferente que
print("Operadores Comparación !=")
print(numA != numB)
print(55 != 55)
print("Operadores Comparación >=")
# Quinto ">=" Mayor o igual que
print(numA >= numB)
print(45 >= 68)
print(67 >= 67)


# Sexto "<=" Menor o igual
print(numA <= numB)
print(89 <= 67)
print(40 <= 40)




# Operadores lógicos

# AND
print("Operadores lógicos AND")

print(25 >= 34 and 67 == 67)
print(67 != 67 and True)
print(numA > numB and "carro" == "carro")
print(10 > 45 and 45 == 35)
print(True and 20 == 20)
print("casa" == "casa" and 45 != 89)
print(89 < 100.1 and 78 < 78)

# OR
print("Operadores lógicos OR")

print(25 >= 34 or 67 == 67)
print(67 != 67 or True)
print(numA > numB or "carro" == "carro")
print(89 == 23 or 189 < 400)
print(10 > 45 or 45 == 35)
print(True or 20 == 20)
print("casa" == "casa" or 45 != 89)
print(89 < 100.1 or 78 < 78)

# NOT
print("Operadores lógicos NOT ")

print(not(56 == 56))
print(not(True))
print(not(45 == 45))
print(89 < 100.1 or not(78 < 78))
print(not(True))
