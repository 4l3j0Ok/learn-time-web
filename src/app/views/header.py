import reflex as rx
from app.components.search import search_bar
from app.styles.common import HEADER_STYLE


def header() -> rx.Component:
    return rx.grid(
        rx.box(
            rx.heading("Learn Time", style=HEADER_STYLE.get("rx_heading")),
            rx.text(
                "By ",
                rx.link(
                    "Alejoide",
                    href="https://alejoide.com",
                ),
            ),
            search_bar(),
            style=HEADER_STYLE,
        )
    )
