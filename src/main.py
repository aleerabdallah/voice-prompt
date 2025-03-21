import flet as ft


async def main(page: ft.Page):
    page.adaptive = True
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "ChatBot"
    page.padding = 0

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

    new_message = ft.TextField(
        hint_text="Let's chat",
        color="#2e3440",
        max_lines=4,
        min_lines=1,
        expand=True,
        multiline=True,
        border=ft.InputBorder.NONE,
    )
    send_prompt_btn = ft.IconButton(icon=ft.Icons.ARROW_UPWARD, bgcolor="#2e3440")
    add_btn = ft.IconButton(icon=ft.Icons.ADD, bgcolor="#2e3440")
    chat.controls.append(ft.Text("Hey! How's it going", color="white"))
    page.add(
        chat,
        ft.Container(
            ft.Column(
                [
                    new_message,
                    ft.Row(
                        [add_btn, send_prompt_btn],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ]
            ),
            bgcolor="#303030",
            border_radius=20,
            padding=9,
            adaptive=True,
        ),
    )


ft.app(main)
