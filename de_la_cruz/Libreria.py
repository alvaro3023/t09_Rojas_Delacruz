#ejercicio 01
def distancia(velocidad,tiempo):
    res = velocidad * tiempo
    return res

#fin_def

#ejercicio 02
def mayor(velocidad,tiempo):
    if (velocidad > tiempo):
        return velocidad
    else:
        return tiempo
#fin_def

def menor(velocidad,tiempo):
    if (tiempo < velocidad):
        return tiempo
    else:
        return velocidad
#fin_def

#ejercicio 03
def obtener_condicion(nota_final):
    if nota_final >= 10.5:
        return "aprobado"
    else:
        return "desaprobado"
#fin_def

#ejercicio 04
def pedir_edad(msg):
    edad = 0
    while (edad <= 0 or edad >= 100):
        edad = int(input("Ingrese edad:"))
        #fin_while
        return edad

#ejrcicio 05
def promedio_unidad(nota_1,nota_2,nota_3):
    if promedio_unidad != 11:
        return "aprobado"
    else:
        return "desaprobado"

#ejercicio 06
def area_base(lado1,lado2):
    area_base_cubo = lado1 * lado2
    return area_base_cubo

def volumen(lado1,area_base_cubo):
    vol_cubo = lado1 * area_base_cubo
    return vol_cubo

#ejercicio 07
def mostrar_ticket(nombre,peli,monto):
    print("#############################")
    print("# CINE PLANET #")
    print("#############################")
    print("# Cliente : " + str(nombre) + " #")
    print("# Pelicula: " + str(peli) + "#")
    print("# Monto : " + str(monto) + " #")
    print("#############################")

#ejercicio 08
def mostrar_precios(Labial_rojo,Sombras,Lapiz_negro,Base,Rubor):
    print("#############################################")
    print("################# UNIKE #####################")
    print("#############################################")
    print("##### Precios:                        ######")
    print("#Labial rojo: ", Labial_rojo)
    print("#Sombras:", Sombras)
    print("#Lapiz negro: ", Lapiz_negro)
    print("#Base: ", Base)
    print("#Rubor: ", Rubor)

#ejercicio 09
def mostrar_carta(ceviche,sudados,arroz_mariscos,refresco_lima,ocopa):
    print("#############################################")
    print("# CEVICHERIA - SEÑOR DELFIN ")
    print("#############################################")
    print("#########         CARTA             #########")
    print("#Ceviche ", ceviche)
    print("#Sudados: ", sudados)
    print("#Arroz con mariscos: ", arroz_mariscos)
    print("#refresco de lima: ", refresco_lima)
    print("#ocopa: ", ocopa)

#ejercicio 10
def total_alumnos(mujeres,hombres):
    total_alumnos=(mujeres+hombres)
    return total_alumnos
#fin_total_alumnos

#ejercicio 11
def puntaje_admision(p_minimo,p_complementario):
    puntaje_admision=(p_minimo+p_complementario)
    return puntaje_admision

#fin_def

#ejercicio 12
def total_alumnos(mujeres,hombres):
    total_alumnos=(mujeres+hombres)
    return total_alumnos
#fin_total_alumnos

#ejercicio 14
def mostrar_utiles(Boligrafo,Cuaderno,Corrector,Juego_escuadras,Portafolio):
    print("#############################################")
    print("# LIBRERIA AMYS")
    print("#############################################")
    print("## OFRECEMOS:                              ##")
    print("#Boligrafo: ", Boligrafo)
    print("#Cuaderno:", Cuaderno)
    print("#Corrector: ",Corrector)
    print("#Juego de escuadras: ", Juego_escuadras)
    print("#Portafolio: ", Portafolio)

def mostrar_prendas(Camisa,Saco,Corbata,Chaleco,Correa):
    print("#############################################")
    print("# SASTERIA EL BUEN VESTIR")
    print("#############################################")
    print("#Camisa: ", Camisa)
    print("#Saco:", Saco)
    print("#Corbata: ", Corbata)
    print("#Chaleco: ", Chaleco)
    print("#Correa: ", Correa)

def mostrar_boleta(Tipo_gasolina,Precio):
    print("#############################################")
    print("# GRIFO PRIMAX")
    print("#############################################")
    print("#Tipo de gasolina: ",Tipo_gasolina)
    print("#Precio del galon: ", Precio)


#ejercicio 17
def mayor(talla_Manuel,talla_Maria):
    if (talla_Manuel > talla_Maria):
        return talla_Manuel
    else:
        return talla_Maria
#fin_def

def menor(talla_Manuel,talla_Maria):
    if (talla_Manuel < talla_Maria):
        return talla_Manuel
    else:
        return talla_Maria
#fin_def

#ejercicio 18
def pedir_año(msg):
    año = 0
    while (año == 2019):
        año = int(input("Ingrese año actual:"))
        #fin_while
        return año

#ejercicio 19
def area_rectangulo(base,altura):
    area = base * altura
    return area

#ejercicio 20
def area_triangulo(base,altura):
    area = base * altura
    return area
