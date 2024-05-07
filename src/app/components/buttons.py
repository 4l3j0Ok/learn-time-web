import reflex as rx
from .react.icons import iconify
from app.styles import common


class ButtonState(rx.State):
    clicked: bool = False

    def toggle(self):
        self.clicked = not self.clicked


def button(element: rx.Var) -> rx.Component:
    title = element["title"]
    icon = element["icon"]
    md_content = element["content"]
    return rx.grid(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.box(
                    iconify(
                        icon,
                        style=common.LANG_ICON,
                        on_click=ButtonState.toggle,
                    ),
                )
            ),
            rx.dialog.content(
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
