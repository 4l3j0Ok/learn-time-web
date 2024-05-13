import reflex as rx
from app.styles.common import TABLIST
from app.components.react.icons import iconify


def view(technology: dict) -> rx.Component:
    return (
        header(technology),
        tablist(technology),
    )


def header(technology: dict) -> rx.Component:
    return rx.grid(
        rx.heading(
            iconify(technology["icon"], display="inline"),
            " ",
            technology["title"],
            text_align="center",
        ),
    )


def tablist(technology: dict = None) -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Información", value="overview"),
            rx.tabs.trigger(rx.text("Recomendaciones"), value="recommendations"),
            rx.tabs.trigger("Recursos", value="resources"),
        ),
        rx.tabs.content(
            rx.markdown(technology["content"]),
            value="overview",
        ),
        rx.tabs.content(
            rx.markdown("# Recomendaciones"),
            value="recommendations",
        ),
        rx.tabs.content(
            rx.markdown("# Recursos"),
            value="resources",
        ),
        default_value="overview",
    )


def resources(technology):
    pass
