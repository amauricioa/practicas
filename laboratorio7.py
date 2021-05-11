""" Laboratorio 7 La tienda de a esquina V 1
    Mauricio Agudelo
    11/05/2021 """

# Definición de Funciones


def sumar_numeros(numero_uno, numero_dos):
    """
    Parameters
    ----------
    numero_uno:float
       operando uno para la suma
    numero_dos:float
       operando dos para la suma
    Returns
    -------
    suma:float
      el resultado de la suma
    """
    suma = numero_uno+numero_dos
    return suma


def restar_numeros(numero_uno, numero_dos):
    '''
    Parameters
    ----------
    numero_uno:float
       operado uno para la resta
    numero_dos:float
       operado dos para la resta
    Returns
    -------
    resta:float
       el resultado de la resta
    '''
    resta = numero_uno-numero_dos
    return resta


def multiplicar_numeros(numero_uno, numero_dos):
    '''
    Parameters
    ----------
    numero_uno:float
       operado uno para la multiplicación
    numero_dos:float
       operado dos para la multiplicación
    Returns
    -------
    resta:float
       el resultado de la multiplicación
    '''
    multiplicacion = numero_uno*numero_dos
    return multiplicacion


def dividir_numeros(numero_uno, numero_dos):
    '''
    Parameters
    ----------
    numero_uno:float
       operado uno para la división
    numero_dos:float
       operado dos para la división
    Returns
    -------
    resta:float
       el resultado de la división
    '''
    division = numero_uno/numero_dos
    return division


numero_uno = float(input("Digite el numero 1:"))
numero_dos = float(input("Digite el numero 2:"))

resultado_suma = sumar_numeros(numero_uno, numero_dos)
resultado_resta = restar_numeros(numero_uno, numero_dos)
resultado_multiplicacion = multiplicar_numeros(numero_uno, numero_dos)
resultado_division = dividir_numeros(numero_uno, numero_dos)

print("la suma es", resultado_suma)
print("la resta es", resultado_resta)
print("la multiplicación es", resultado_multiplicacion)
print("la división es", resultado_division)
