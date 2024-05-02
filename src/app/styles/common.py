import reflex as rx
from .fonts import Font


STYLESHEETS = [
    f"https://fonts.googleapis.com/css2?family={Font.Default.value}:ital,wght@0,100..900;1,100..900&display=swap",
]

BASE = {
    "font_family": Font.Default.value,
    rx.markdown: {
        "font_family": Font.Default.value,
        "h1, h2, h3, h4, h5, h6": {Font.Default.value},
    },
    rx.heading: {
        "font_family": Font.Default.value,
        "margin_y": "2em",
    },
}


LANG_ICON = {
    "width": "100%",
    "height": "100%",
    "background_color": "orange",
    "color": "white",
    "border_radius": "50%",
    "padding": "1em",
    "overflow": "visible",
    "cursor": "pointer",
    ":hover": {
        "background_color": "white",
        "color": "orange",
    },
    "transition": ".3s ease-in-out",
}
