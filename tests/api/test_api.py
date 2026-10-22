"""NIVEL DE INTEGRACIÓN (API) — Playwright APIRequestContext.

Objeto de prueba: el contrato HTTP de /api/... (rutas, códigos de estado, JSON).
Fixtures disponibles (ver tests/conftest.py):
    api               -> cliente sin token
    api_autenticada   -> cliente con token válido
Los datos se reinician antes de cada prueba (3 productos iniciales, ids 1, 2 y 3).

Ejecuta solo este nivel:   pytest tests/api -v
"""


# ---------------------------------------------------------------- EJEMPLO
def test_listar_productos_devuelve_los_tres_iniciales(api_autenticada):
    respuesta = api_autenticada.get("/api/productos")
    assert respuesta.status == 200
    assert len(respuesta.json()) == 3


# ------------------------------------------------------------- CONSULTAR
def test_consultar_producto_inexistente_devuelve_404(api_autenticada):
    r = api_autenticada.get("/api/productos/999")
    assert r.status == 404
