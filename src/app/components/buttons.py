import reflex as rx
from .react.icons import iconify
from app.styles import common
from app.states import TechnologyType


def button(technology: TechnologyType, as_link: bool = False) -> rx.Component:
    return rx.grid(
        iconify(
            technology.icon,
            on_click=rx.redirect(technology.page) if as_link else None,
            style=common.LANG_BUTTON,
        ),
        rx.text(
            technology.title,
            margin_top=".25em",
        ),
        class_name=common.ANIMATIONS["zoom_in"],
        place_items="center",
    )
