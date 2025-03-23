import asyncio
import flet as ft
import time
from ollama import AsyncClient


async def main(page: ft.Page):
    page.adaptive = True
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "ChatBot"
    page.padding = ft.padding.only(top=80, bottom=0)

    page.bgcolor = "#212121"
    chat = ft.ListView(auto_scroll=True, expand=True, padding=10, spacing=10)

    chat.padding = ft.padding.only(right=26, left=26)
    welcoming = ft.Container(
        content=ft.Row(
            [
                ft.Text(
                    value="What's your question?",
                    color="white",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    # text_align=ft.TextAlign.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        margin=ft.margin.only(top=240),
        alignment=ft.Alignment(0.0, 0.0),
        # bgcolor="blue",
        adaptive=True,
    )
    new_message = ft.TextField(
        hint_text="Let's chat",
        color="#444444",
        max_lines=4,
        min_lines=1,
        expand=True,
        multiline=True,
        border=ft.InputBorder.NONE,
        # on_submit=
    )

    async def send_prompt(e):
        print(f"Hello: {e}")
        # if message.value == "" or message.value == None
        print(new_message.value)
        welcoming.visible = False
        chat.controls.append(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text(
                            f"{new_message.value}",
                            # text_align=ft.TextAlign.END,
                            color="white",
                            bgcolor="#2e3440",
                            expand=20,
                            size=15,
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
        new_message.value = ""
        page.update()
        time.sleep(1)
        text = ft.Text(value="", color="white", size=15)
        chat.controls.append(text)
        page.update()

        async def get_response(prompt="Hello"):
            message = {"role": "user", "content": f"{prompt}"}
            async for part in await AsyncClient().chat(
                model="tinyllama", messages=[message], stream=True
            ):
                # print(part["message"]["content"], end="")
                text.value += part["message"]["content"]
                text.update()

        await get_response(new_message.value)

    send_prompt_btn = ft.IconButton(
        icon=ft.Icons.ARROW_UPWARD,
        bgcolor="#2e3440",
        on_click=send_prompt,
    )
    add_btn = ft.IconButton(icon=ft.Icons.ADD, bgcolor="#2e3440")

    page.add(
        welcoming,
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
            padding=18,
            adaptive=True,
        ),
    )


ft.app(main)
