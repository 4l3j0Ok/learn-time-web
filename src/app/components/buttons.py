import reflex as rx
from .react.icons import iconify
from app.styles import common


def button(technology: rx.Var) -> rx.Component:
    title = technology["title"]
    icon = technology["icon"]
    md_content = technology["content"]
    return rx.grid(
        rx.dialog.root(
            rx.dialog.trigger(
                iconify(
                    icon,
                    style=common.LANG_BUTTON,
                )
            ),
            rx.dialog.content(
                rx.dialog.close(
                    iconify(
                        "carbon:close-filled",
                        style=common.CLOSE_BUTTON,
                    ),
                ),
                rx.markdown(
                    md_content,
                    component_map=common.MD_COMPONENT_MAP,
                ),
                style=common.BASE[rx.dialog.content],
            ),
        ),
        rx.text(
            title,
            margin_top=".25em",
        ),
        class_name=common.ANIMATIONS["zoom_in"],
        place_items="center",
    )
