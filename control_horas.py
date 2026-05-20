# ============================================
# Programa: Control de Horas Semanales
# Descripción:
# Calcula el total de horas trabajadas
# por cada recurso y clasifica su jornada.
# ============================================

# Matriz con los recursos y horas trabajadas
# [Nombre, lunes, martes, miércoles, jueves, viernes]

recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 8, 7, 8],
    ["Luis", 9, 9, 10, 8, 9],
    ["María", 6, 7, 8, 7, 6]
]

# Función para calcular total y clasificación
def calcular_horas(recurso):
    nombre = recurso[0]
    horas = recurso[1:]

    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total, clasificacion


# Mostrar resultados
print("===== REPORTE DE HORAS SEMANALES =====\n")

for recurso in recursos:
    nombre, total, clasificacion = calcular_horas(recurso)

    print(f"Recurso: {nombre}")
    print(f"Total Horas: {total}")
    print(f"Clasificación: {clasificacion}")
    print("-----------------------------------")