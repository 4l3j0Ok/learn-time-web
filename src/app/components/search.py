import reflex as rx
from app.views.langs import ElementsState


def search_bar() -> rx.Component:
    return (
        rx.input(
            placeholder="¿Qué vas a aprender hoy?",
            radius="full",
            width="50vw",
            font_size="1em",
            padding="2em",
            on_change=ElementsState.set_elements,
        ),
    )
