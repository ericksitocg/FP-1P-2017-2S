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
