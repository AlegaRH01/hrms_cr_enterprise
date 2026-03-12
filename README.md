
# HRMS Costa Rica Enterprise 🇨🇷

Sistema de **Gestión de Recursos Humanos y Nómina para Costa Rica** desarrollado en Python, diseñado para cumplir con la legislación laboral costarricense y facilitar el cálculo automático de planillas.

Este proyecto implementa lógica de nómina basada en regulaciones del **Código de Trabajo de Costa Rica**, incluyendo deducciones obligatorias, cálculo de aguinaldo, y liquidaciones laborales.

---

# Características principales

## Gestión de nómina

* Cálculo automático de **CCSS empleado y patrono**
* Cálculo de **impuesto sobre la renta salarial**
* Cálculo de **INS riesgos del trabajo**
* Cálculo de **aguinaldo**
* Cálculo de **vacaciones pendientes**
* Cálculo de **cesantía**

## Reportes

* Reporte de planilla
* Exportación contable
* Estructura para reportes legales

## API REST

Incluye API para integrar el sistema con otras plataformas.

Ejemplo:

POST `/calcular_planilla`

```json
{
  "salario": 1000000
}
```

Respuesta:

```json
{
  "salario_bruto": 1000000,
  "ccss": 106700,
  "renta": 0,
  "salario_neto": 893300
}
```

## Arquitectura SaaS

Incluye base para:

* múltiples empresas
* múltiples empleados
* sistema de recursos humanos tipo SaaS

---

# Estructura del proyecto

```
hrms_cr_enterprise/
   payroll/
      ccss.py
      ins.py
   tax/
      renta.py
   liquidaciones/
      liquidacion.py
   reports/
      planilla.py
   accounting/
      export.py
   saas/
      multiempresa.py
   fixtures/
      salary_components.json

app.py
docker-compose.yml
requirements.txt
INSTALL.md
```

---

# Instalación rápida con Docker

1. Instalar Docker

2. Ejecutar:

```
docker compose up
```

3. Abrir en el navegador:

```
http://localhost:8000
```

---

# Ejemplo de uso de la API

Calcular planilla:

```
POST /calcular_planilla
```

Body:

```json
{
 "salario": 1200000
}
```

---

# Tecnologías utilizadas

* Python
* Flask
* Docker
* REST API

---

# Roadmap del proyecto

Próximas mejoras:

* Panel administrativo web
* Gestión de empleados
* Control de asistencia
* Gestión de vacaciones
* Generación de colillas de pago PDF
* Reportes legales completos
* Portal del empleado
* Versión SaaS multiempresa

---

# Licencia

Proyecto open source bajo licencia MIT.

---

# Autor

Desarrollado para proyectos de **automatización de recursos humanos y nómina en Costa Rica**.

---

# Contribuciones

Las contribuciones son bienvenidas.
Puedes abrir un **Issue** o enviar un **Pull Request**.

---

# Aviso legal

Este software proporciona cálculos de nómina basados en reglas generales de Costa Rica.
Siempre se recomienda validar los resultados con un contador o especialista en legislación laboral.
