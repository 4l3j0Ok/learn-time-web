import reflex as rx
from app.views.header import header
from app.modules.constants import Languages, DevOps
from app.pages.not_found import not_found


class RouteState(rx.State):
    @rx.var
    def technology(self) -> str:
        return self.router.page.params.get("technology")

    @rx.var
    def technologies(self) -> list:
        technologies = []
        technologies.extend(Languages.items.value.keys())
        technologies.extend(DevOps.items.value.keys())
        return technologies


@rx.page("/[technology]")
def index() -> rx.Component:
    return rx.cond(
        RouteState.technologies.contains(RouteState.technology),
        header(),
        not_found(),
    )
