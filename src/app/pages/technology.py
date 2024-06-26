import reflex as rx
from app.views.technology import view
from app.views.footer import footer
from app.pages.not_found import not_found
from app.states import TechnologiesState
from app.styles.common import ANIMATIONS
from app.modules.constants import App


@rx.page("/[technology]", title=App.name_with_nick.value)
def technology() -> rx.Component:
    return rx.box(
        rx.cond(
            TechnologiesState.selected,
            rx.container(
                view(TechnologiesState.selected),
                class_name=ANIMATIONS.get("zoom_in"),
            ),
            not_found(),
        ),
        footer(),
    )
