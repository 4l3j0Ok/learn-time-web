import reflex as rx
from app.styles.common import BUTTON


def not_found() -> rx.Component:
    return rx.grid(
        rx.grid(
            rx.heading("404", margin_y="0", font_size="5em"),
            rx.heading("Página no encontrada.", margin_top="1.5em", size="4"),
            rx.text("La página que buscas no existe."),
            rx.link(
                rx.box("Volver al inicio", margin_top="3em", style=BUTTON),
                href="/",
            ),
        ),
        height="80vh",
        width="100%",
    )
