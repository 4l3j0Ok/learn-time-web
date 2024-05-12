import reflex as rx


def view(technology: dict) -> rx.Component:
    return (
        header(technology),
        tablist(technology),
    )


def header(technology: dict) -> rx.Component:
    return rx.grid(rx.heading(technology["title"]))


def tablist(technology: dict = None) -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Información", value="overview"),
            rx.tabs.trigger("Recomendaciones", value="tab2"),
            rx.tabs.trigger("Recursos", value="tab3"),
        ),
        rx.tabs.content(
            rx.markdown(technology["content"]),
            value="overview",
        ),
        rx.tabs.content(
            rx.markdown("# Recomendaciones"),
            value="tab2",
        ),
        rx.tabs.content(
            rx.markdown("# Recursos"),
            value="tab3",
        ),
        default_value="overview",
    )


def resources(technology):
    pass
