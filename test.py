from typing import Coroutine
from ollama import AsyncClient
import asyncio


async def chat(message):
    message = {"role": "user", "content": f"{message}"}
    async for part in await AsyncClient().chat(
        model="tinyllama", messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)
        # await websocket.send_bytes(part['message']['content'])


async def main():
    await chat("What's large language model in brief")


async def sync_to_async(func):

    async def wrapper(e, message):
        message = {"role": "user", "content": f"{message}"}
        async for part in await AsyncClient().chat(
            model="tinyllama", messages=[message], stream=True
        ):
            print(part["message"]["content"], end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
