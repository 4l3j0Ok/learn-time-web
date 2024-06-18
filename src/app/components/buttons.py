import reflex as rx
from .react.icons import iconify
from app import styles
from app.states import TechnologyType


def button(technology: TechnologyType, as_link: bool = False) -> rx.Component:
    return rx.grid(
        iconify(
            technology.icon,
            on_click=rx.redirect(technology.page) if as_link else None,
            style=styles.finder.TECHNOLOGY_BUTTON,
        ),
        rx.text(
            technology.title,
            margin_top=".25em",
        ),
        class_name=styles.common.ANIMATIONS["zoom_in"],
        place_items="center",
    )
