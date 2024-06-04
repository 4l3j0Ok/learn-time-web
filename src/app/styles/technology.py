from app.styles.colors import Palette


COURSES_CARDS = {
    "max_width": "25em",
    "background_color": Palette.background.value,
    "color": Palette.white.value,
    "transition": ".3s ease-in-out",
    ":hover": {
        "background_color": Palette.accent.value,
        "color": Palette.white.value,
    },
    "cursor": "pointer",
    "image": {
        "width": "100%",
        "object_fit": "cover",
    },
}

COURSES_GRID = {
    "flex_wrap": "wrap",
    "gap": "1em",
    "justify_content": "center",
}

RESOURCES_CARDS = {
    "width": "25em",
    "height": "10em",
    "padding": "1em",
    "margin_bottom": "1em",
    "background_color": Palette.background.value,
    "color": Palette.white.value,
    "transition": ".3s ease-in-out",
    ":hover": {
        "background_color": Palette.accent.value,
        "color": Palette.white.value,
    },
    "icon": {
        "height": "100%",
        "width": "30%",
    },
    "cursor": "pointer",
}

RESOURCES_GRID = {
    "flex_wrap": "wrap",
    "gap": "1em",
    "justify_content": "center",
}
