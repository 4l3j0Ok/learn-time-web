import reflex as rx
from app.styles.common import BUTTON


def not_found() -> rx.Component:
    return rx.grid(
        rx.grid(
            rx.heading("404", margin_y="0", font_size="5em"),
            rx.heading("Página no encontrada.", margin_top="1.5em", size="4"),
            rx.text("La página que buscas no existe."),
            rx.link("Volver al inicio", href="/", margin_top="3em", style=BUTTON),
        ),
        height="100vh",
        width="100vw",
    )
