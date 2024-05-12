import reflex as rx
from app.components.buttons import button
from app.components.search import search_bar
from app.styles.common import ELEMENTS_GRID, HEADER_STYLE
from app.modules.constants import Languages, DevOps
from app.states import TechnologiesState
from app.views.footer import footer


def view() -> rx.Component:
    return (
        header(),
        langs(),
        devops(),
        more_soon(),
        footer(),
    )


def header() -> rx.Component:
    return rx.grid(
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


def langs() -> rx.Component:
    return rx.cond(
        TechnologiesState.langs,
        rx.grid(
            rx.heading(Languages.title.value),
            rx.flex(
                rx.foreach(
                    TechnologiesState.langs,
                    lambda technology: button(technology, as_link=True),
                ),
                style=ELEMENTS_GRID,
            ),
        ),
    )


def devops() -> rx.Component:
    return rx.cond(
        TechnologiesState.devops,
        rx.grid(
            rx.heading(DevOps.title.value),
            rx.flex(
                rx.foreach(
                    TechnologiesState.devops,
                    lambda technology: rx.box(
                        button(
                            technology,
                            **DevOps.items.value.get(f"{technology}", {}),
                        )
                    ),
                ),
                style=ELEMENTS_GRID,
            ),
        ),
    )


def more_soon() -> rx.Component:
    return rx.center(
        rx.heading("Más próximamente..."),
    )
