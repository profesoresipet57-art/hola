import flet as ft

def main(page: ft.Page):
    page.title = "Hola Mundo en Flet Web"
    page.add(ft.Text("🌐 ¡Hola, mundo desde Flet Web!", size=30, color="green"))

# Ejecutar como web app
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
