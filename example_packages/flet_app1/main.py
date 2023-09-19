
from contextlib import asynccontextmanager

import flet as ft
import flet_fastapi_proxy_path as flet_fastapi
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)



val = 1



@app.get("/about")
async def about():
    return {"message": "Hello World"}


@app.get("/set/{value}")
async def set(value:str = None):
    global val
    val = value
    return {'message': 'ok'}



async def main(page: ft.Page):
    txt_number = ft.TextField(value=val, text_align=ft.TextAlign.RIGHT, width=200)

    async def btnClicked(e):
        txt_number.value = val
        await txt_number.update_async()

    await page.add_async(
        ft.Column(
            [
                ft.Text("Hello, Flet!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=btnClicked),
            ]
        )
    )


appName = 'app1'

app.mount("/", flet_fastapi.app(main, proxy_path=f'/{appName}'))



