import flet as ft


async def main(page: ft.Page):
    page.adaptive = True
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "ChatBot"
    page.bgcolor = "#212121"
    chat = ft.ListView(auto_scroll=True, expand=True, padding=10, spacing=10)

    chat.controls.append(ft.Container(padding=20))

    chat.controls.append(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        "Hi, what's going on with you",
                        # text_align=ft.TextAlign.END,
                        color="white",
                        bgcolor="#2e3440",
                        expand=20,
                    ),
                    bgcolor="#2e3440",
                    # alignment=ft.alignment.top_right,
                    padding=10,
                    border_radius=20,
                )
            ],
            alignment=ft.MainAxisAlignment.END,
        )
    )

    new_message = ft.TextField(hint_text="Let's chat")
    chat.controls.append(ft.Text("Hey! How's it going", color="white"))
    page.add(chat)


ft.app(main)
