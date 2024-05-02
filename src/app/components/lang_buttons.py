import reflex as rx
import os
from .react.icons import iconify
from app.styles import common


class ButtonState(rx.State):
    clicked: bool = False

    def toggle(self):
        self.clicked = not self.clicked


def lang_button(language: str, lang_name: str = None, custom_icon: str = None):
    lang_name = language.capitalize() if not lang_name else lang_name
    icon_pack = "simple-icons"
    icon = f"{icon_pack}:{language}" if not custom_icon else custom_icon
    logo = iconify(
        icon,
        style=common.LANG_ICON,
        on_click=ButtonState.toggle,
    )
    markdown_file = f"{os.getenv('SRC_PATH')}/app/langs/{language}.md"
    markdown = open(markdown_file).read()
    return rx.box(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.box(
                    rx.box(logo),
                ),
            ),
            rx.dialog.content(rx.markdown(markdown)),
        ),
        rx.text(
            lang_name,
            margin_top=".25em",
        ),
        text_align="center",
    )
