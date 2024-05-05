import reflex as rx
from app.components.search import search_bar


def header() -> rx.Component:
    return rx.grid(
        rx.box(
            rx.heading("Learn Time", font_size="5em", margin_y=".25em"),
            rx.text("By ", rx.link("Alejoide", href="https://alejoide.com")),
            search_bar(),
            text_align="center",
            margin_y="2em",
        ),
        place_items="center",
    )
