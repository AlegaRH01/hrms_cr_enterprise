
def calcular_renta(salario):

    if salario <= 941000:
        return 0

    if salario <= 1381000:
        return (salario - 941000) * 0.10

    if salario <= 2423000:
        return (1381000 - 941000) * 0.10 + (salario - 1381000) * 0.15

    return (1381000 - 941000) * 0.10 + (2423000 - 1381000) * 0.15 + (salario - 2423000) * 0.20
