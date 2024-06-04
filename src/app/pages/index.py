import reflex as rx
from app.views.finder import view
from app.styles.common import ANIMATIONS
from app.views.footer import footer


@rx.page("/", title="Learn Time by Alejoide")
def index() -> rx.Component:
    return rx.box(
        rx.container(
            view(),
            class_name=ANIMATIONS.get("zoom_in"),
        ),
        footer(),
    )
