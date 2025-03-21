import flet as ft


async def main(page: ft.Page):
    page.adaptive = True
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "ChatBot"

    chat = ft.ListView(auto_scroll=True, expand=True)


ft.app(main)
