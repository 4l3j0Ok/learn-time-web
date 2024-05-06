import reflex as rx
from .views.header import header
from .views.elements import langs, devops, more_soon
from .views.footer import footer
from .styles import common


@rx.page("/", title="Learn Time by Alejoide")
def index() -> rx.Component:
    return (
        header(),
        langs(),
        devops(),
        more_soon(),
        footer(),
    )


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
