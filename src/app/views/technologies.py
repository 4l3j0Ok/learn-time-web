import reflex as rx
from app.components.buttons import button
from app.styles.common import ELEMENTS_GRID
from app.modules.constants import Languages, DevOps


class TechnologiesState(rx.State):
    user_filter: str = ""
    langs_technologies: list[dict] = [item for item in Languages.items.value.values()]
    devops_technologies: list[dict] = [item for item in DevOps.items.value.values()]

    def set_technologies(self, value: str):
        self.user_filter = value
        self.langs_technologies = [
            item
            for item in Languages.items.value.values()
            if value.lower() in item["title"].lower()
        ]
        self.devops_technologies = [
            item
            for item in DevOps.items.value.values()
            if value.lower() in item["title"].lower()
        ]


def langs() -> rx.Component:
    return rx.cond(
        TechnologiesState.langs_technologies,
        rx.grid(
            rx.heading(Languages.title.value),
            rx.flex(
                rx.foreach(
                    TechnologiesState.langs_technologies,
                    lambda technology: button(technology),
                ),
                style=ELEMENTS_GRID,
            ),
        ),
    )


def devops() -> rx.Component:
    return rx.cond(
        TechnologiesState.devops_technologies,
        rx.grid(
            rx.heading(DevOps.title.value),
            rx.flex(
                rx.foreach(
                    TechnologiesState.devops_technologies,
                    lambda technology: rx.box(
                        button(
                            technology,
                            **DevOps.items.value.get(f"{technology}", {}),
                        )
                    ),
                ),
                style=ELEMENTS_GRID,
            ),
        ),
    )


def more_soon() -> rx.Component:
    return rx.center(
        rx.heading("Más próximamente..."),
    )
