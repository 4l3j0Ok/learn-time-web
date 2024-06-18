import reflex as rx
from app.views.finder import view
from app.styles.common import ANIMATIONS
from app.views.footer import footer
from app.modules.constants import App


@rx.page("/", title=App.name_with_nick.value)
def index() -> rx.Component:
    return rx.box(
        rx.container(
            view(),
            class_name=ANIMATIONS.get("zoom_in"),
        ),
        footer(),
    )
