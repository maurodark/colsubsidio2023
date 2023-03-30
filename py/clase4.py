for w in (1,2,3,4):
  print(w)

for w in "1,2,3,4":
  print(w)

for w in "Dagoberto":
  print(w)

"""**FUNCIÓN Range(start, stop, step)**

cuando solo se pasa 1 parámetro a la función Range por default (stop)
"""

for i in range(0,11,3):
  print(i)

nombre = input("Digite su nombre: ")

for i in range(9):
  print(i, nombre)

"""Escribir un programa que realice la tabla de multiplicar de un número digitado por teclado"""

num = int(input("Digite el número de la tyabla de multiplicar: "))
for i in range(11):
  print(i, " x ", num , " = ", i * num)

"""Escriba un programa que me sume los números pares del 0 al 10 y saque el total de la suma."""

# variable acumuladora
acu = 0

for i in range(0,11,2):
  # print(i)
  acu = acu + i
print(f"El total de la suma de los números pares del 0-10= {acu}")

"""**Taller Refuerzo**
Ejercicios: https://drive.google.com/file/d/1L2Tn9iTSnSJlskALvM2hBpOBUEJdcwLL/view?usp=sharing

3. Escribir un programa que pregunte al usuario su edad y
muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad). ciclo for
"""

edad = int(input("Por favor, ingrese su edad: "))

print("Usted ha cumplido los siguientes años:")

for i in range(1, edad+1):
    print(i)

"""Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números
impares desde 1 hasta ese número separados por comas.
"""

numero = int(input("Digite  un número entero positivo: "))
enteros_positivos   
for i in range(1,numero,2):
  num = numero
  print("Los números impares desde 1 hasta",num,"son:",i)

numero = int(input("Por favor, ingrese un número entero positivo: "))

impares = ""

for i in range(1, numero+1, 2):
    impares += str(i) + ", "

print("Los números impares desde 1 hasta", numero, "son:", impares[:-2])

"""Encuentra la suma de todos los números pares del 1 al
100 ciclo for
"""

suma = 0
for i in range(2, 101, 2):
    #suma += i
    suma = suma + i
print("La suma de todos los números pares del 1 al 100 es:", suma)




