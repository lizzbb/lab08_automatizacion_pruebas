"""NIVEL UNITARIO (componente) — pytest puro.

Objeto de prueba: app/validaciones.py (funciones puras, sin servidor ni navegador).
Técnicas sugeridas: partición de equivalencia y análisis de valores límite.

Ejecuta solo este nivel:   pytest tests/unitarias -v
"""
from app.validaciones import validar_credenciales, validar_producto


# ---------------------------------------------------------------- EJEMPLO
def test_credenciales_con_formato_valido_no_tienen_errores():
    assert validar_credenciales("admin", "Admin123") == []


# ----------------------------------------------------------- PRODUCTO
def test_precio_cero_es_invalido():
    # Límite: el precio debe ser MAYOR que 0.
    assert validar_producto("Teclado", 0, 1) != []
