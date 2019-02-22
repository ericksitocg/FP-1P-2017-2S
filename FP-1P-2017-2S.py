#Autor Erick Humberto Cordova Gavilanes
#Tema 1
import numpy as np

"""
Su trabajo es planificar la mayor cantidad de tareas que se pueden realizar en un día de 1440 minutos.
Para ello seleccionará las tareas basadas en sus tiempos de finalización prefiriendo las tareas que
terminan más temprano en el día,Asuma que no existen tareas que finalizan en el mismo minuto.

+--------------+
|Tareas del día|
+--------------+
1. Cortar papel de regalos
2. Vestir muñecas
3. …

"""
print("Tema 1")

tareas = ["pintar soldados", "hornear galletas", "armar muñecos", "cortar papel de regalo"]
inicio = [678, 200, 240, 423]
duracion = [300, 800, 456, 112]

A_tareas = np.array(tareas)
A_inicio = np.array(inicio)
A_duracion = np.array(duracion)

A_finalizacion = A_inicio + A_duracion

A_ind_finalizacion = A_finalizacion.argsort()#Ascendente

A_tareas_ordenadas = A_tareas[A_ind_finalizacion]

L_tareas_dia = []

total = 0
for ind in A_ind_finalizacion:
    tarea = A_tareas[ind]
    duracion = A_duracion[ind]
    if total + duracion <= 1440:
        total += duracion
        L_tareas_dia.append(tarea)

print("""
+--------------+
|Tareas del día|
+--------------+
""")

for i in range(len(L_tareas_dia)):
    print("%d. %s"%(i+1,L_tareas_dia[i]))


#Tema 2

"""
El resultado del examen se lo entregan como una cadena de texto. Los indicadores los puede
identificar porque estos siempre estarán en mayúsculas, por ejemplo INR, WBC, RBC, TA, etc. Todo
indicador va seguido de un espacio, luego un número con decimales, seguido de otro espacio en blanco y
finalmente las unidades. Al final del resultado se encuentra el nombre del médico. 

La cantidad de indicadores puede variar. Los puntos no solo aparecen en los decimales, sino también
para separar párrafos o en otras ocasiones como las direcciones de e-mail

Escriba un programa que nos muestre la información desglosada, el nombre del médico y una
recomendación de si el paciente debe ir al endocrinólogo. Un paciente debe ir al endocrinólogo si su nivel
de azúcar (BGT), está por encima de los 150 mmol/dL. En caso de dar la recomendación, mostrar doble
asterisco en el indicador BGT y la recomendación al final. 

INFORME DE LABORATORIO
**********************
INR 1.25 segundos
BGT 180.12 mmol/dL **
HGB 13 g/dL
ESR 3.2 mm/hora
RBC 4000024.2 cel/uL
TA 1.5 ng/dL
WBC 123233.23 cel/uL
Médico: Juan Pozo
**Su nivel de azúcar es alto, se recomienda ir al endocrinólogo.
"""

print("Tema 2")
resultado = "Resultado de Laboratorio ‘Su Salud’ Nombre del paciente: Jose Aimas E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC 123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firma médico responsable Dr. Juan Pozo"

L_palabras = resultado.split(" ")
L_indicadores = []
L_cantidades = []
L_unidades = []
azucar_alto = False

for i in range(len(L_palabras)):
    palabra = L_palabras[i]
    if palabra.isupper():
        L_indicadores.append(palabra)

        cantidad = L_palabras[i +1]
        unidades = L_palabras[i + 2]

        if palabra == "BGT":
            if float(cantidad) > 150:
                unidades += " **"
                azucar_alto = True

        L_cantidades.append(cantidad)
        L_unidades.append(unidades)
    elif palabra.lower() == "dr." or palabra.lower() == "dra.":
        L_datos_doctor = L_palabras[i + 1:]
        nombre_doctor = " ".join(L_datos_doctor)

print("""
INFORME DE LABORATORIO
**********************
""")

for i in range(len(L_indicadores)):
    print("%s%15.3f\t\t%s"%(L_indicadores[i],float(L_cantidades[i]),L_unidades[i]))
print()
print("Medico: %s"%nombre_doctor)
if azucar_alto:
    print("**Su nivel de azúcar es alto, se recomienda ir al endocrinólogo.")

#Tema 3
print("Tema 3\n")

L_datos = [[239034,678493,896321,32438,554213],[4568321,6745634,9754008,3242342,3456123],[234773,56743,123678,4783,90874],[45672,45212,90781,3904,90431]]
M = np.array(L_datos)

tipoGasolina = np.array(["Regular", "Extra", "Super", "Premium"])
gasolineras = np.array(['Primax Alborada', 'PS Los Ríos', 'Mobil Cumbaya', 'Lutexsa CIA Ltda','PS Remigio Crespo'])
distrito = np.array(['distrito1', 'distrito2', 'distrito1','distrito2','distrito4'])
ciudades = np.array(['Guayaquil', 'Babahoyo' , 'Quito' , 'Guayaquil', 'Cuenca'])

#1. Pida un tipo de gasolina por teclado y muestre por pantalla los nombres de todas
#las gasolineras que han vendido en el año más del promedio de venta en galones para ese tipo.

gasolina = input("Ingrese un tipo de gasolina: ").capitalize()
#CORREGIR No usar tolist
A_bol = tipoGasolina.tolist().index(gasolina)
A_ventas_gasolina = M[A_bol,:]
promedio_gasolina = A_ventas_gasolina.mean()

A_nombres =gasolineras[A_ventas_gasolina > promedio_gasolina]

print(A_nombres)

#[13 puntos] Pida una ciudad por teclado y calcule cuántas de sus gasolineras han vendido más de
#15 millones de galones en total en el año, considerando todas las ventas de todos los tipos de
#gasolinas.

ciudad = input("Ingrese una ciudad: ").capitalize()
A_indices_ciudad = ciudades == ciudad
A_ventas_ciudad = M[:,A_indices_ciudad].sum(axis=0)
print(A_ventas_ciudad)
numero_gasolineras_condicion = A_ventas_ciudad[A_ventas_ciudad > 15000000].size

print("Existen %d gasolineras con más de 15 millones de galones en total en el año en la ciudad de %s"%(numero_gasolineras_condicion,ciudad))

#3. [20 puntos] Muestre por pantalla el nombre de la ciudad que más galones ha vendido en el año
#de gasolina tipo Diesel en el distrito distrito1.

#Tema 4
print("Tema 4.1")
f = ['a', 'c', 'z', 'm', 'k']
g = [3,4,5,6,5,7]
t = ''

for c in f:
    a = f.index(c)
    b = g[:a]
    t = t + (c * len(b))
    print(t)
print("Tema 4.2")
vector = np.array([1, 5, 6, 6, 5, 2, 1, 3, 7, 9, 0, 0, 1, 4, 8])
print(np.unique(vector[vector % 2 == 0]).size)