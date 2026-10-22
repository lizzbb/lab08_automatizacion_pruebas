# Informe · Laboratorio 8 · Pruebas automatizadas

**Equipo:** (número)

**Integrantes:** 
- Lizbeth Andrea Herrera Ortega - 1246024 
- Marcela Nicole Letran Lee - 1102124
- Bruno Antonio Urías Castillo - 1184524
- Zane Christian Bran Lockridge - 1373724

## 1. Defectos encontrados

Un reporte por defecto. Deja la prueba que lo detecta FALLANDO en tu entrega.

| ID | Nivel que lo detectó | Prueba (archivo::función) | Pasos para reproducir | Resultado esperado (según la especificación) | Resultado obtenido |
|---|---|---|---|---|---|
| DEF-01 |Unitarias |tests/unitarias/test_unitarias.py::test_precio_cero_es_invalido |Editar o crear producto -> Ingresar precio 0 -> Guardar |No debe aceptar el precio y guardar producto | Si se guarda el producto con precio 0 |
| DEF-02 |API |tests/api/test_api.py::test_consultar_producto_inexistente_devuelve_404 |Consultar producto inexistente desde metodo HTTP |Que devuelva codigo de error 404, no existe |Devuelve codigo 200, OK |
| DEF-03 |E2E |tests/e2e/test_e2e.py::test_eliminar_producto_borra_solo_ese_producto | Iniciar sesión -> Elegir producto -> Eliminar| Se elimina el producto seleccionado|Se elimina el producto anterior, no el que se selecciona |

## 2. Tabla comparativa de niveles

Tiempo: ejecuta `pytest tests/<nivel> -q` y anota el tiempo que reporta pytest.

| Criterio | Unitarias | API | E2E |
|---|---|---|---|
| Número de pruebas |2| | |
| Tiempo total de ejecución (s) |0.52s | | |
| Tiempo promedio por prueba (s) | 0.52s| | |
| Defectos detectados (IDs) |DEF-01 | | |
| ¿Qué cambio en la app rompería estas pruebas sin que haya un defecto? | | | |
| Costo de mantenimiento (Alto / Medio / Bajo) y por qué | | | |

## 3. Recomendación (máximo media página)

El equipo de Inventario IS1 tiene un pipeline de CI. Recomienda qué pruebas correr:

- en cada commit,
- en cada pull request,
- antes de liberar a producción.

Justifica con tus datos de la tabla y con la pirámide de pruebas.
Responde además: ¿qué defecto NO habría detectado una suite solo de pruebas E2E, o solo de pruebas unitarias?
