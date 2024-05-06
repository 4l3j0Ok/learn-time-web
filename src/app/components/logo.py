import reflex as rx
from app.modules.constants import App


def logo(with_link=True, **kwargs) -> rx.Component:
    return (
        rx.link(
            rx.image(
                src="/alejoide.svg",
                href=App.url.value,
                is_external=True,
                **kwargs,
            )
        )
        if with_link
        else rx.image(
            src="/alejoide.svg",
            **kwargs,
        )
    )
