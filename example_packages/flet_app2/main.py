
from contextlib import asynccontextmanager

import flet as ft
import flet_fastapi_proxy_path as flet_fastapi
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()


appName = 'app2'


app = FastAPI(lifespan=lifespan)


@app.get("/about")
async def about():
    return {"message": f"Hello from Fastapi {appName}"}


async def main(page: ft.Page):
    await page.add_async(ft.Text(f"Hello from Flet {appName}"))


app.mount("/", flet_fastapi.app(main, proxy_path=f'/{appName}'))
