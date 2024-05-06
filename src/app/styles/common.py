import reflex as rx
from .fonts import Font


STYLESHEETS = [
    f"https://fonts.googleapis.com/css2?family={Font.Default.value}:ital,wght@0,100..900;1,100..900&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
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
    rx.grid: {
        "place_items": "center",
    },
}

ANIMATIONS = {
    "zoom_in": "animate__animated animate__zoomIn animate__faster",
}

LANG_ICON = {
    "width": "5em",
    "height": "5em",
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

ELEMENTS_GRID = {
    "width": "50vw",
    "flex_wrap": "wrap",
    "gap": "2em",
    "justify_content": "center",
}

HEADER_STYLE = {
    "text_align": "center",
    "margin_y": "2em",
    "rx_heading": {
        "font_size": "5em",
        "margin_y": ".25em",
    },
}

SEARCH_BAR = {
    "width": "50vw",
    "margin_top": "2em",
    "rx_input": {
        "font_size": "1em",
        "padding": "2em",
    },
}

FOOTER = {
    "width": "100%",
    "margin_top": "8em",
    "margin_bottom": "2em",
}
