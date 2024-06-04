import reflex as rx
from app.components.react.icons import iconify


def course(
    title: str = "",
    subtitle: str = "",
    image: str = "",
    image_style: dict = {},
    badge_text: str = "",
    inset_side: str = "top",
    **kwargs,
) -> rx.Component:
    return rx.card(
        rx.cond(
            bool(badge_text),
            rx.badge(
                badge_text,
                variant="solid",
                position="fixed",
                top="0",
                right="0",
                margin="1em",
            ),
        ),
        rx.inset(
            rx.image(
                src=image,
                alt=title,
                style=image_style,
            ),
            side=inset_side,
        ),
        rx.box(
            rx.heading(title, margin_y=".5em", size="5"),
            rx.text(subtitle),
        ),
        **kwargs,
    )


def resource(
    title: str = "",
    subtitle: str = "",
    icon: str = "",
    icon_style: dict = {},
    **kwargs,
):
    return rx.card(
        rx.flex(
            rx.cond(
                icon,
                iconify(
                    icon,
                    style=icon_style,
                ),
            ),
            rx.box(
                rx.heading(title, margin_y=".5em", size="5"),
                rx.text(subtitle),
                margin_left="1.5em",
                width="100%",
            ),
            height="100%",
        ),
        **kwargs,
    )
