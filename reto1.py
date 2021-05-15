""" Reto 1 - protegiendo el castillo V1
    Mauricio Agudelo
    15/05/2021 """


# Funciones
def bienvenida():
    """
    Returns
    -------
      Mensaje de bienvenida
    """
    print("="*100)
    print("Bienvenido rey Arturito, con este programa lograran realizar los calculos, para cerrar",
          "la puerta \ny mantener seguro el castillo.")
    print("="*100)


def convertir_mts_cms(largo_puerta):
    """
    Parameters
    ----------
    largo_puerta:float
       operando para calculo de conversión
    Returns
    -------
    largo_puerta_cms:float
      resultado de conversion de metros a centimetros
    """
    factor_coversion_cms = 100
    largo_puerta_cms = largo_puerta * factor_coversion_cms
    return largo_puerta_cms


def convertir_min_seg(minutos):
    """
    Parameters
    ----------
    minutos:float
       operando para calculo de conversión
    Returns
    -------
    segundos:float
      resultado de conversion de minutos a segundos
    """
    segundos = minutos * 60
    return segundos


def calcular_radio(diametro_polea):
    """
    Parameters
    ----------
    diamtro_polea:float
       operando para calculo de radio
    Returns
    -------
    radio_polea:float
      calculo de radio en base a un diametro
    """
    radio_polea = diametro_polea / 2
    return radio_polea


def calcular_vueltas(diametro_polea, largo_puerta):
    """
    Parameters
    ----------
    diametro_polea:float
       diametro de la polea
    largo_puerta:float
       largo en mtrs de la puerta
    Returns
    -------
    numero_vuelta:float
      calculo de numero de vueltas con base a radio y
      largo de la puerta
    """
    pi = 3.1416
    largo_puerta_cms = convertir_mts_cms(largo_puerta)
    radio_poela = calcular_radio(diametro_polea)
    numero_vueltas = largo_puerta_cms / (pi*radio_poela)
    return numero_vueltas


def calcular_numero_soldados(numero_vueltas, vueltas_soldados):
    """
    Parameters
    ----------
    numero_vueltas:float
       numero de vuletas de la polea
    vueltas_soldados:float
       vueltas de cada soldado
    Returns
    -------
    numero_soldados:float
      calculo de numero de vueltas con base a radio y
      largo de la puerta
    """
    numero_soldados = numero_vueltas / vueltas_soldados
    return numero_soldados


def calcular_velocidad_polea(tiempo_minutos, largo_puerta):
    """
    Parameters
    ----------
    tiempo_minutos:float
       minutos maximos
    largo_puerta:float
       cantidad de cuerda a recoger
    Returns
    -------
    velocidad:float
      velocidad de la polea en cms/seg
      con tiempo dado
    """
    largo = convertir_mts_cms(largo_puerta)
    segundos = convertir_min_seg(tiempo_minutos)
    velocidad = largo/segundos
    return velocidad


# Inicio
bienvenida()
print("\n\nAntes de empezar, necesito que digites los siguientes datos:")
largo_puerta_mtr = float(input("\n¿Cuantos metros mide la puerta? "))
diametro_polea = float(
    input("¿Cuantos Centimetros de diametro mide la polea? "))
tiempo_minutos = float(input("¿En cuantos minutos debe cerrar? "))

# Salida
numero_vueltas = calcular_vueltas(largo_puerta_mtr, diametro_polea)
vueltas_soldados = 3

print("\n")
print("+-"*50)
print("\nCon los datos suministrados tengo los siguientes calculos para usted: \n")

print("Se requieren ", numero_vueltas,
      "vueltas para cerrar completamente la puerta")
print("Se necesitan ", calcular_numero_soldados(numero_vueltas, vueltas_soldados),
      "soldados para cerrar completamente la puerta")
print("Con un tiempo", tiempo_minutos, "minutos, la polea giraría a",
      calcular_velocidad_polea(tiempo_minutos, largo_puerta_mtr), "cms/seg")
