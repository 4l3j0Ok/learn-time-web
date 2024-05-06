import reflex as rx
from app.views.elements import ElementsState
from app.styles.common import SEARCH_BAR


def search_bar() -> rx.Component:
    return rx.box(
        rx.input(
            placeholder="¿Qué vas a aprender hoy?",
            on_change=ElementsState.set_elements,
            style=SEARCH_BAR.get("rx_input"),
        ),
        style=SEARCH_BAR,
    )
