import reflex as rx
import app.pages
from .styles import common
from app.pages import index
from app.pages.not_found import not_found


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="full",
        accent_color=common.Palette.color_scheme.value,
    ),
    stylesheets=common.STYLESHEETS,
    style=common.BASE,
)
app.add_custom_404_page(not_found(), title="Página no encontrada")
