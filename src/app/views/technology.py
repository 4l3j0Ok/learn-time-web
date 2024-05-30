import reflex as rx
from app.components.react.icons import iconify
from app.components import cards
from app.states import TechnologyType
from app.styles.common import CARDS, CARDS_GRID


def view(technology) -> rx.Component:
    return (
        header(technology),
        tablist(technology),
    )


def header(technology: TechnologyType) -> rx.Component:
    return rx.grid(
        rx.heading(
            iconify(technology.icon, display="inline"),
            " ",
            technology.title,
            text_align="center",
        ),
    )


def tablist(technology=None) -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Información", value="overview"),
            rx.tabs.trigger("Cursos", value="learn"),
            rx.tabs.trigger("Recursos", value="resources"),
        ),
        rx.tabs.content(
            rx.markdown(technology.content),
            value="overview",
        ),
        rx.tabs.content(
            course(technology),
            value="learn",
        ),
        rx.tabs.content(
            resources(technology),
            value="resources",
        ),
        default_value="overview",
    )


def course(technology: TechnologyType) -> rx.Component:
    courses = rx.foreach(
        technology.courses,
        lambda course: rx.link(
            rx.cond(
                course["is_free"],
                cards.with_badge(
                    title=course["title"],
                    subtitle=f"Creador: {course['author']}",
                    image=course["image"],
                    image_style=CARDS["image"],
                    badge_text="Gratuito",
                    style=CARDS,
                ),
                cards.simple(
                    title=course["title"],
                    subtitle=f"Creador: {course['author']}",
                    image=course["image"],
                    image_style=CARDS["image"],
                    style=CARDS,
                ),
            ),
            href=f"{course["url"]}",
            is_external=True,
        ),
    )
    return rx.grid(
        rx.flex(
            courses,
            style=CARDS_GRID,
        ),
    )


def resources(technology) -> rx.Component:
    return rx.box()
