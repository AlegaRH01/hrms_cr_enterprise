
def generar_reporte(empleados):
    reporte = []
    for e in empleados:
        reporte.append({
            "empleado": e["nombre"],
            "salario": e["salario"]
        })
    return reporte
