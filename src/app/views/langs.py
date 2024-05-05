import reflex as rx
from app.components.buttons import Button
from app.styles.common import ELEMENTS_GRID
from app.modules.constants import Languages, DevOps


class ElementsState(rx.State):
    user_filter: str = ""
    langs_elements: list[dict] = [item for item in Languages.ITEMS.value.values()]
    devops_elements: list[dict] = [item for item in DevOps.ITEMS.value.values()]

    def set_elements(self, value: str):
        self.user_filter = value
        self.langs_elements = [
            item
            for item in Languages.ITEMS.value.values()
            if value.lower() in item["title"].lower()
        ]
        self.devops_elements = [
            item
            for item in DevOps.ITEMS.value.values()
            if value.lower() in item["title"].lower()
        ]


def langs() -> rx.Component:
    return rx.cond(
        ElementsState.langs_elements,
        rx.grid(
            rx.heading(Languages.TITLE.value),
            rx.flex(
                rx.foreach(
                    ElementsState.langs_elements,
                    lambda element: Button.create(element),
                ),
                style=ELEMENTS_GRID,
            ),
        ),
    )


def devops() -> rx.Component:
    return rx.cond(
        ElementsState.devops_elements,
        rx.grid(
            rx.heading(DevOps.TITLE.value),
            rx.flex(
                rx.foreach(
                    ElementsState.devops_elements,
                    lambda element: rx.box(
                        Button.create(
                            element,
                            **DevOps.ITEMS.value.get(f"{element}", {}),
                        )
                    ),
                ),
                style=ELEMENTS_GRID,
            ),
        ),
    )
