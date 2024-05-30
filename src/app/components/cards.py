import reflex as rx


def simple(
    title: str = "",
    subtitle: str = "",
    image: str = "",
    image_style: dict = {},
    **kwargs,
) -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(src=image, alt=title, style=image_style),
            side="top",
            pb="current",
        ),
        rx.box(
            rx.heading(title, margin_y=".5em", size="5"),
            rx.text(subtitle),
        ),
        **kwargs,
    )


def with_badge(
    title: str = "",
    subtitle: str = "",
    image: str = "",
    badge_text: str = "",
    image_style: dict = {},
    **kwargs,
) -> rx.Component:
    return rx.card(
        rx.badge(
            badge_text,
            variant="solid",
            position="fixed",
            top="0",
            right="0",
            margin="1em",
        ),
        rx.inset(
            rx.image(src=image, alt=title, style=image_style),
            side="top",
            pb="current",
        ),
        rx.box(
            rx.heading(
                title,
                size="5",
                margin_y=".5em",
            ),
            rx.text(subtitle),
        ),
        **kwargs,
    )
