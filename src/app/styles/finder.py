from app.styles.colors import Palette


TECHNOLOGY_BUTTON = {
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

TECHNOLOGY_GRID = {
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
        "height": "4em",
        "text_align": "center",
        "font_size": "1em",
        "color": Palette.white.value,
    },
}
