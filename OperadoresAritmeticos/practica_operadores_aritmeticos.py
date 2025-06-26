"""
Reto 1 - Suma - total compras:
Contexto:
“Luis compró un libro y un cuaderno para el colegio. ¿Cuánto debe pagar en total?”
Enunciado:
Define dos variables: precio_libro (valor: 12.99) y precio_cuaderno (valor: 5.50).
Calcula el total de las compra usando el operador +
Muestra el resultado con print()
"""

# Definir las variables del reto

print("[+] Reto 1 - Suma - Total Compras")

precio_libro = 12.99 # variable con  tipo de dato float
precio_cuaderno = 5.50 # variable con tipo de dato float

# Creando una variable calculo_total que va a realizar el computo de sumar 
# precio_libro + precio_cuaderno
calculo_total = precio_libro + precio_cuaderno

# Mostrando al usuario el total a pagar y usando funcion round() para redondear
print("[+] El total a pagar es de: ", round(calculo_total), " dolares")

"""
Reto 2 - Multiplicación - Porciones pastel:
Contexto:
“En una fiesta, un pastel se dividió en 8 porciones iguales. Si 3 personas comen 2 porciones
cada, ¿Cuántas porciones se consumieron en total?”
Enunciado:
Define variables para las personas (valor: 3) y las porciones_por_personas (valor: 2)
Calcula el total de porciones consumidas usando el operador *
Imprime el resultado con un mensaje como: “Porciones consumidas: [resultado]”
"""

# Definiendo las variables del reto 2
print("[+] Reto 2 - Multiplicación - Porciones pastel")

personas = 3 # variable de tipo entera 
porciones_por_personas = 2 # variable de tipo entera 

# Definiendo una nueva variable total_porciones que va realizar el computo de
# multiplicar personas * porciones_por_personas 

total_porciones = personas * porciones_por_personas 

# Mostrando con un  print total_porciones consumidas del pastel

print("[+] Las 3 personas han consumido un total de: ", total_porciones ," porciones")

"""
Reto 3 - Desafío rápido:
Contexto:
“Ana quiere resolver esta operación matemática: (10 + 2) * 3/4. ¿Cuál es el resultado?”
Enunciado:
Asigna la operación (10 + 2) * 3 / 4 a una variable llamada resultado
Imprime el valor de resultado con print()
"""

# Definiendo las variables del reto 3 
print("[+] Reto 3 - Desafío rápido")

operacion = (10 + 2) * 3 / 4 
# Mostrando el resultado de la operacion 

print("[+] El resulta de la siguiente operacion [(10 + 2) * 3 / 4] es =", operacion)