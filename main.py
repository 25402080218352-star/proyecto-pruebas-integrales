def pedir_datos():
    nombre = input("Ingresa el nombre del alumno: ")
    grupo = input("Ingresa el grupo: ")
    cal1 = float(input("Ingresa la calificación 1: "))
    cal2 = float(input("Ingresa la calificación 2: "))
    cal3 = float(input("Ingresa la calificación 3: "))
    return nombre, grupo, cal1, cal2, cal3
#Modulo de calculos y validación
def calcular_promedio(cal1, cal2, cal3):
    return (cal1 + cal2 + cal3) / 3

def obtener_estado(promedio):
    if promedio >= 7:
        return "Aprobado"
    else:
        return "Reprobado"

nombre, grupo, cal1, cal2, cal3 = pedir_datos()
promedio = calcular_promedio(cal1, cal2, cal3)
estado = obtener_estado(promedio)

print("\n--- RESULTADO FINAL ---")
print("Nombre:", nombre)
print("Grupo:", grupo)
print("Promedio final:", round(promedio, 2))
print("Estado:", estado)
