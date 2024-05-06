import reflex as rx
from .views.header import header
from .views.langs import langs, devops
from .views.footer import footer
from .styles import common


@rx.page("/")
def index() -> rx.Component:
    return rx.box(
        header(),
        langs(),
        devops(),
        footer(),
    )


app = rx.App(
    stylesheets=common.STYLESHEETS,
    style=common.BASE,
)
