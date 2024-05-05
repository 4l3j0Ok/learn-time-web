import reflex as rx
from .views.header import header
from .views.langs import langs, devops
from .styles import common


@rx.page("/")
def index() -> rx.Component:
    return rx.box(
        header(),
        langs(),
        devops(),
    )


app = rx.App(
    theme=rx.theme(
        accent_color="orange",
        has_background_color=True,
    ),
    stylesheets=common.STYLESHEETS,
    style=common.BASE,
)
