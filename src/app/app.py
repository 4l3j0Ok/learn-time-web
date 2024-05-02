import reflex as rx
from .views.langs import langs
from .styles import common


@rx.page("/")
def index():
    return rx.box(
        langs(),
    )


app = rx.App(
    theme=rx.theme(
        accent_color="orange",
        has_background_color=True,
    ),
    stylesheets=common.STYLESHEETS,
    style=common.BASE,
)
