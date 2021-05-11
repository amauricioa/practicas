'''Laboratorio 5
   Mauricio Agudelo
   11/05/2021'''

# Escribi un programa que leea varios detos y luego los imprima

# Captura de datos
nombre = input("Digita tu nombre: ")
fecha_nacimiento = input("Digita tu fecha de nacimiento: ")
age = int(input("Digita tu edad: "))
ocupacion = input("Digita tu ocupacion: ")
direccion_casa = input("Digita la direccion de tu casa: ")
numero_personas_vives = int(input("Con cuantas personas vives? "))
estado_civil = input("Estado civil: ")

# impresion de datos
print("tu nombre es", nombre)
print("naciste el", fecha_nacimiento)
print("tienes", age, "años de edad")
print("tu oficio es", ocupacion)
print("la direccion de tu casa es ", direccion_casa)
print("vives con", numero_personas_vives, "personas")
print("y tu estado civil es", estado_civil)
