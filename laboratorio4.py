# Calculo del IMC
print("*** Aplicativo que te indica tu IMC *** \n")
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en Kilogramos: "))
# Sigue el programa aqui
imc = peso/altura**2
print("\nTu IMC (Indice de Masa Corporal) es:", imc)
