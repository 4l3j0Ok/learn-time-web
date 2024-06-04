from datetime import date
import reflex as rx
from app.modules.constants import App
from app.components.logo import logo
from app.styles.footer import FOOTER


def footer() -> rx.Component:
    return rx.grid(
        logo(with_link=False, style=FOOTER["logo"]),
        rx.text(
            f"2024 - {date.today().year}"
            if date.today().year > 2024
            else "2024" + " © ",
            rx.link(f"{App.name.value} by {App.author.value}", href=App.url.value),
            " v1.",
            margin_bottom=".5em",
        ),
        style=FOOTER,
    )
