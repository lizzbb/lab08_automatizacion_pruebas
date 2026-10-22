"""NIVEL DE SISTEMA (E2E) — Playwright en un navegador real.

Objeto de prueba: los flujos del usuario en la interfaz web.
La fixture `page` la provee pytest-playwright; las rutas relativas usan base_url.
Los datos se reinician antes de cada prueba.

Ejecuta solo este nivel:          pytest tests/e2e -v
Para VER el navegador:            pytest tests/e2e --headed --slowmo 500
Para grabar interacciones:        playwright codegen http://127.0.0.1:5000
                                  (con la app corriendo: python run.py)
"""
from playwright.sync_api import Page, expect


def iniciar_sesion(page: Page, usuario="admin", password="Admin123"):
    page.goto("/login")
    page.get_by_label("Usuario").fill(usuario)
    page.get_by_label("Contraseña").fill(password)
    page.get_by_role("button", name="Ingresar").click()


def fila(page: Page, texto):
    return page.get_by_role("row").filter(has_text=texto)


# ---------------------------------------------------------------- EJEMPLO
def test_pagina_de_login_carga(page: Page):
    page.goto("/login")
    expect(page.get_by_role("heading", name="Iniciar sesión")).to_be_visible()


# ------------------------------------------------------------------ CRUD
def test_eliminar_producto_borra_solo_ese_producto(page: Page):
    iniciar_sesion(page)
    fila(page, "Mouse").get_by_role("button", name="Eliminar").click()

    expect(page.get_by_text("Producto eliminado")).to_be_visible()
    expect(fila(page, "Mouse")).to_have_count(0)
    # Sin efectos colaterales sobre los demás registros.
    expect(fila(page, "Teclado")).to_have_count(1)
    expect(fila(page, "Monitor")).to_have_count(1)
