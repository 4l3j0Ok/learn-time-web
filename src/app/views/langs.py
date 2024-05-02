import reflex as rx
from app.components.lang_buttons import lang_button


def langs(title="Lenguajes") -> rx.Component:
    return rx.grid(
        rx.heading(title),
        rx.grid(
            lang_button("python"),
            lang_button(
                "javascript",
                lang_name="JavaScript",
                custom_icon="material-symbols:javascript",
            ),
            lang_button("csharp", lang_name="C#"),
            lang_button("java", custom_icon="ri:java-line"),
            lang_button("html", custom_icon="akar-icons:html-fill"),
            lang_button("cplusplus", lang_name="C++"),
            lang_button("typescript", lang_name="TypeScript"),
            lang_button("go"),
            lang_button("c", lang_name="C"),
            lang_button("rust"),
            lang_button("ruby"),
            lang_button("php", lang_name="PHP", custom_icon="devicon-plain:php"),
            lang_button("dart"),
            lang_button("kotlin", custom_icon="cib:kotlin"),
            lang_button("swift"),
            gap="3em",
            grid_template_columns="repeat(auto-fit, minmax(75px, 1fr))",
            width="75vw",
        ),
        place_items="center",
    )
