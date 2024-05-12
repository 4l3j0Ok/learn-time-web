import reflex as rx
from .fonts import Font
from .colors import Palette


STYLESHEETS = [
    f"https://fonts.googleapis.com/css2?family={Font.Default.value}:ital,wght@0,100..900;1,100..900&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
]

BASE = {
    "display": "flex",
    "flex_direction": "column",
    "min_height": "100vh",
    "background_color": Palette.background.value,
    "color": Palette.white.value,
    "font_family": Font.Default.value,
    rx.text: {
        "color": Palette.white.value,
        "font_family": Font.Default.value,
    },
    rx.dialog.content: {
        "background_color": Palette.background.value,
        "color": Palette.white.value,
        "min_width": "min-content",
    },
    rx.heading: {
        "font_family": Font.Default.value,
        "margin_y": "2em",
    },
    rx.grid: {
        "place_items": "center",
    },
    rx.link: {
        "color": Palette.accent.value,
        "text_decoration": "none",
        ":hover": {
            "color": Palette.white.value,
        },
        "transition": ".3s ease-in-out",
    },
}

ANIMATIONS = {
    "zoom_in": "animate__animated animate__zoomIn animate__faster",
}

BUTTON = {
    "background_color": Palette.accent.value,
    "color": Palette.white.value,
    "padding": "1em",
    "overflow": "visible",
    "cursor": "pointer",
    "border_radius": "2em",
    ":hover": {
        "background_color": Palette.white.value,
        "color": Palette.accent.value,
    },
    "transition": ".3s ease-in-out",
}

LANG_BUTTON = {
    "width": "5em",
    "height": "5em",
    "border_radius": "50%",
    "background_color": Palette.accent.value,
    "color": Palette.white.value,
    "padding": "1em",
    "overflow": "visible",
    "cursor": "pointer",
    ":hover": {
        "background_color": Palette.white.value,
        "color": Palette.accent.value,
    },
    "transition": ".3s ease-in-out",
}

CLOSE_BUTTON = {
    "height": "2em",
    "width": "max-content",
    "position": "sticky",
    "top": "1em",
    "margin-left": "auto",
    "background_color": Palette.white.value,
    "color": Palette.accent.value,
    "overflow": "visible",
    "cursor": "pointer",
    "border_radius": "2em",
    ":hover": {
        "background_color": Palette.accent.value,
        "color": Palette.white.value,
    },
    "transition": ".3s ease-in-out",
}

ELEMENTS_GRID = {
    "width": ["80vw", "80vw", "80vw", "50w", "50vw"],
    "flex_wrap": "wrap",
    "gap": "2em",
    "justify_content": "center",
}

HEADER_STYLE = {
    "text_align": "center",
    "margin_top": "5em",
    "margin_bottom": "2em",
    "rx_heading": {
        "font_size": ["3em", "5em"],
        "margin_y": ".25em",
    },
}

SEARCH_BAR = {
    "width": "100%",
    "max_width": ["80vw", "80vw", "80vw", "50w", "50vw"],
    "margin_top": "2em",
    "rx_input": {
        "text_align": "center",
        "font_size": "1em",
        "padding": "2em",
        "color": Palette.white.value,
    },
}

FOOTER = {
    "padding": "10em 0 2em 0",
    "margin_top": "auto",
    "logo": {
        "width": "15em",
        "height": "auto",
        "margin_bottom": "1em",
    },
}

MD_COMPONENT_MAP = {
    "p": lambda text: rx.text(
        text,
        style=BASE[rx.text],
    ),
    "h1": lambda text: rx.heading(
        text,
        size="6",
        style=BASE[rx.heading],
        margin_y="1em",
    ),
    "h2": lambda text: rx.heading(
        text,
        size="5",
        style=BASE[rx.heading],
        margin_y="1em",
    ),
    "h3": lambda text: rx.heading(
        text,
        size="4",
        style=BASE[rx.heading],
        margin_y="1em",
    ),
    "h4": lambda text: rx.heading(
        text,
        size="3",
        style=BASE[rx.heading],
        margin_y="1em",
    ),
    "h5": lambda text: rx.heading(
        text,
        size="2",
        style=BASE[rx.heading],
        margin_y="1em",
    ),
    "h6": lambda text: rx.heading(
        text,
        size="1",
        style=BASE[rx.heading],
        margin_y="1em",
    ),
}
