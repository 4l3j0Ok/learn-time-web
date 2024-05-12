import reflex as rx
from .react.icons import iconify
from app.styles import common


def button(technology: rx.Var, as_link: bool = False) -> rx.Component:
    title = technology["title"]
    icon = technology["icon"]
    return rx.grid(
        iconify(
            icon,
            on_click=rx.redirect(technology["page"]) if as_link else None,
            style=common.LANG_BUTTON,
        ),
        rx.text(
            title,
            margin_top=".25em",
        ),
        class_name=common.ANIMATIONS["zoom_in"],
        place_items="center",
    )
