from datetime import date
import reflex as rx
from app.modules.constants import App
from app.components.logo import logo
from app.styles.common import FOOTER


def footer() -> rx.Component:
    return rx.grid(
        logo(
            with_link=False,
            width="15em",
            height="auto",
            margin_bottom="2em",
        ),
        rx.text(
            f"2024 - {date.today().year}"
            if date.today().year > 2024
            else "2024" + f" © {App.name.value} by {App.author.value}",
            margin_bottom=".5em",
        ),
        style=FOOTER,
    )
