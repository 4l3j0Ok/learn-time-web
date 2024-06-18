import reflex as rx
from app.modules.constants import Misc
from app.components.react.icons import iconify
from app.components import cards
from app.styles.technology import BACK_BUTTON
from app.states import TechnologyType
from app.styles.technology import (
    COURSES_CARDS,
    COURSES_GRID,
    RESOURCES_CARDS,
    RESOURCES_GRID,
)


def view(technology) -> rx.Component:
    return rx.box(
        header(technology),
        tablist(technology),
    )


def back_button() -> rx.Component:
    return rx.link(
        iconify(Misc.back_button_icon.value, style=BACK_BUTTON),
        href="/",
    )


def header(technology: TechnologyType) -> rx.Component:
    return rx.box(
        back_button(),
        rx.grid(
            rx.heading(
                iconify(technology.icon, display="inline"),
                " ",
                technology.title,
                text_align="center",
            ),
        ),
    )


def tablist(technology: TechnologyType) -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Información", value="overview"),
            rx.cond(
                technology.courses,
                rx.tabs.trigger("Cursos", value="courses"),
            ),
            rx.cond(
                technology.resources,
                rx.tabs.trigger("Recursos", value="resources"),
            ),
        ),
        rx.tabs.content(
            rx.markdown(technology.content),
            value="overview",
        ),
        rx.cond(
            technology.courses,
            rx.tabs.content(
                rx.grid(
                    rx.flex(
                        rx.foreach(
                            technology.courses,
                            lambda course: course_card(course),
                        ),
                        style=COURSES_GRID,
                    ),
                ),
                value="courses",
            ),
        ),
        rx.cond(
            technology.resources,
            rx.tabs.content(
                rx.grid(
                    rx.flex(
                        rx.foreach(
                            technology.resources,
                            lambda resource: resource_card(resource),
                        ),
                        style=RESOURCES_GRID,
                    )
                ),
                value="resources",
            ),
        ),
        default_value="overview",
    )


def course_card(course) -> rx.Component:
    return rx.link(
        rx.cond(
            course["is_free"],
            cards.course(
                title=course["title"],
                subtitle=f"Creador: {course['author']}",
                image=course["image"],
                image_style=COURSES_CARDS["image"],
                badge_text="Gratuito",
                style=COURSES_CARDS,
            ),
            cards.course(
                title=course["title"],
                subtitle=f"Creador: {course['author']}",
                image=course["image"],
                image_style=COURSES_CARDS["image"],
                style=COURSES_CARDS,
            ),
        ),
        href=f"{course["url"]}",
        is_external=True,
    )


def resource_card(resource) -> rx.Component:
    return rx.link(
        cards.resource(
            title=resource["title"],
            subtitle=resource["description"],
            icon=resource["icon"],
            icon_style=RESOURCES_CARDS["icon"],
            style=RESOURCES_CARDS,
        ),
        href=f"{resource["url"]}",
        is_external=True,
    )
