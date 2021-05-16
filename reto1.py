""" Reto 1 - protegiendo el castillo - v1.0
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


def convertir_mts_cms(metros):
    """
    Parameters
    ----------
    largo_puerta:float
       metros para conversión
    Returns
    -------
    largo_puerta_cms:float
      resultado de conversion de metros a centimetros
    """
    factor_coversion_cms = 100
    centimetros = metros * factor_coversion_cms
    return centimetros


def convertir_min_seg(minutos):
    """
    Parameters
    ----------
    minutos:float
       minutos a convertir
    Returns
    -------
    segundos:float
      resultado de conversión de minutos a segundos
    """
    segundos = minutos * 60
    return segundos


def calcular_radio(diametro_polea):
    """
    Parameters
    ----------
    diametro_polea:float
       operando para calculo de radio
    Returns
    -------
    radio_polea:float
      calculo de radio en base a un diametro
    """
    radio_polea = diametro_polea / 2
    return radio_polea


def calcular_largo_cuerda(largo_puerta, alto_muro):
    """
    Parameters
    ----------
    largo_puerta:float
       largo de la puerta para hallar largo cuerda
    alto_muro:float
        alto del muro para hallar largo cuerda
    Returns
    -------
    largo_cuerda:float
      largo de la cuerda en cms restando diferencia de puerta y muro 
    """
    largo_puerta_cms = convertir_mts_cms(largo_puerta)
    alto_muro_cms = convertir_mts_cms(alto_muro)
    largo_cuerda = (largo_puerta_cms**2+alto_muro_cms**2)**0.5
    print(largo_cuerda)
    largo_cuerda = largo_cuerda - (alto_muro_cms - largo_puerta_cms)
    return largo_cuerda


def calcular_vueltas(radio, largo_puerta, alto_muro):
    """
    Parameters
    ----------
    radio:float
       radio para calculo
    largo_puerta:float
       largo en mtrs de la puerta
    Returns
    -------
    numero_vuelta:float
      calculo de numero de vueltas con base a radio y
      largo de la puerta
    """
    pi = 3.1416
    largo_cuerda = calcular_largo_cuerda(largo_puerta, alto_muro)
    numero_vueltas = largo_cuerda / (pi*radio)
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


def calcular_velocidad_polea(tiempo_minutos, radio):
    """
    Parameters
    ----------
    tiempo_minutos:float
       minutos maximos
    radio:float
        radio de la circunferencia
    Returns
    -------
    velocidad:float
      velocidad a la que gira la polea en cms/seg
    """
    pi = 3.1416
    segundos = convertir_min_seg(tiempo_minutos)
    velocidad = (2*pi*radio)/segundos
    return velocidad


# Inicio
bienvenida()
print("\n\nAntes de empezar, necesito que digites los siguientes datos:")
largo_puerta_mtr = float(input("\n¿Cuantos metros mide la puerta? "))
alto_muro_mtr = float(input("¿Cuantos metros mide el muro? "))
diametro_polea = float(
    input("¿Cuantos centimetros de diametro mide la polea? "))
tiempo_minutos = float(input("¿En cuantos minutos debe cerrar? "))

# Operaciones
radio = calcular_radio(diametro_polea)
numero_vueltas = calcular_vueltas(
    radio, largo_puerta_mtr, alto_muro_mtr)
vueltas_soldados = 3
numero_soldados = calcular_numero_soldados(numero_vueltas, vueltas_soldados)
velocidad_polea = calcular_velocidad_polea(
    tiempo_minutos, radio)

# Salida
print("\n")
print("+-"*50)
print("\nCon los datos suministrados tengo los siguientes calculos para usted: \n")

print("Se requieren ", numero_vueltas,
      "vueltas para cerrar completamente la puerta")
print("Se necesitan ", numero_soldados,
      "soldados para cerrar completamente la puerta")
print("Con un tiempo", tiempo_minutos, "minutos, la polea giraría a",
      velocidad_polea, "cms/seg")
