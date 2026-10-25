# Informe · Laboratorio 8 · Pruebas automatizadas

**Equipo:** 6

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
| DEF-03 |E2E |tests/e2e/test_e2e.py::test_eliminar_producto_borra_solo_ese_producto | Iniciar sesión -> Elegir producto -> Eliminar| Se elimina el producto seleccionado|Se elimina el primer producto de la lista, no el que se selecciona |

## 2. Tabla comparativa de niveles

Tiempo: ejecuta `pytest tests/<nivel> -q` y anota el tiempo que reporta pytest.

| Criterio | Unitarias | API | E2E |
|---|---|---|---|
| Número de pruebas |2|2|2|
| Tiempo total de ejecución (s) |0.52s|2.11s|8.59s|
| Tiempo promedio por prueba (s) |0.26s|1.055s|4.295s|
| Defectos detectados (IDs) |DEF-01 |DEF-02|DEF-03|
| ¿Qué cambio en la app rompería estas pruebas sin que haya un defecto? | Cambiar el nombre o la firma de `validar_producto`, o que devuelva otro tipo en lugar de una lista|Cambiar la ruta o la estructura del JSON |Cambiar textos de botones o etiquetas, la estructura de la tabla o el diseño|
| Costo de mantenimiento (Alto / Medio / Bajo) y por qué |**Bajo**, porque son funciones rápidas y estables|**Medio**, dependen del contrato y del servidor|**Alto**, son pruebas lentas que necesitan el navegador y dependen del HTML|

## 3. Recomendación (máximo media página)

El equipo de Inventario IS1 tiene un pipeline de CI. Recomienda qué pruebas correr:

- en cada commit,
- en cada pull request,
- antes de liberar a producción.

Justifica con tus datos de la tabla y con la pirámide de pruebas.
Responde además: ¿qué defecto NO habría detectado una suite solo de pruebas E2E, o solo de pruebas unitarias?

### Recomendación del equipo

Recomendamos organizar el pipeline siguiendo la pirámide de pruebas: muchas pruebas rápidas y baratas en la base (unitarias), una capa intermedia de pruebas de API y pocas pruebas E2E en la punta. Cada nivel se ejecuta con una frecuencia distinta, según su costo. 

- **En cada commit: pruebas unitarias.** La suite tarda 0.52 s (0.26 s por prueba en promedio), así que el desarrollador tiene la respuesta casi de inmediato. Su mantenimiento es bajo porque prueban funciones puras que solo cambian si cambian las reglas del negocio. Por este nivel se detectó DEF-01 (precio 0 aceptado), el defecto más barato de encontrar.
- **En cada pull request: unitarias + API.** Las pruebas de API tardan 2.11 s y verifican el contrato HTTP (códigos de estado, autenticación, CRUD) sin necesidad de un navegador. Antes de integrar código a la rama principal conviene comprobar que los componentes funcionan juntos. Este nivel detectó DEF-02 (`GET` de un producto inexistente devuelve 200 en vez de 404).
- **Antes de liberar a producción: la suite completa, incluyendo E2E.** Las pruebas E2E son las más lentas (8.59 s, unas 16 veces más que las unitarias) y las más frágiles, porque se rompen si cambia un texto, una etiqueta o la estructura del HTML. Sin embargo, son las únicas que validan los flujos reales del usuario, estas detectaron DEF-03 (el botón "Eliminar" siempre borra el primer producto), un defecto que no aparece en ningún otro nivel.

**¿Qué defecto no habría detectado una suite de un solo nivel?**

- **Solo E2E** no habría detectado **DEF-02**: la interfaz web nunca consulta un producto por su id, así que el 200 en lugar de 404 solo es visible desde la API. DEF-01 sí se vería, pero con una prueba mucho más lenta y costosa que la unitaria.
- **Solo unitarias** no habría detectado **DEF-02 ni DEF-03**: ambos están fuera de `validaciones.py` (en la ruta de la API y en la plantilla HTML), que es el único código que prueban las unitarias.

Ningún nivel por sí solo encontró los tres defectos. Esto justifica una estrategia por capas, la mayoría de las pruebas en los niveles bajos, por velocidad y costo, y pocas E2E para cubrir lo que solo se ve desde la interfaz.
