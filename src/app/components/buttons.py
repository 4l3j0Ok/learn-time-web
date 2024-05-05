import reflex as rx
from .react.icons import iconify
from app.styles import common


class Button(rx.ComponentState):
    clicked: bool = False

    def toggle(self):
        self.clicked = not self.clicked

    @classmethod
    def get_component(
        cls,
        element: rx.Var,
    ) -> rx.Component:
        title = element["title"]
        icon = element["icon"]
        md_content = element["content"]
        return rx.grid(
            rx.dialog.root(
                rx.dialog.trigger(
                    iconify(
                        icon,
                        style=common.LANG_ICON,
                        on_click=cls.toggle,
                    )
                ),
                rx.dialog.content(rx.markdown(md_content)),
            ),
            rx.text(
                title,
                margin_top=".25em",
            ),
        )
