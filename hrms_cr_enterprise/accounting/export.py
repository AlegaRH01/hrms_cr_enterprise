
def exportar(planilla):

    asientos = []

    for p in planilla:

        asientos.append({
            "cuenta": "Gasto salarios",
            "monto": p["salario"]
        })

    return asientos
