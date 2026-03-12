
from flask import Flask, jsonify, request
from hrms_cr_enterprise.payroll.ccss import calcular_ccss_empleado
from hrms_cr_enterprise.tax.renta import calcular_renta

app = Flask(__name__)

@app.route("/calcular_planilla", methods=["POST"])
def calcular():
    data = request.json
    salario = data["salario"]

    ccss = calcular_ccss_empleado(salario)
    renta = calcular_renta(salario)

    return jsonify({
        "salario_bruto": salario,
        "ccss": ccss,
        "renta": renta,
        "salario_neto": salario - ccss - renta
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
