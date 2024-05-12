import reflex as rx
from app.modules.constants import Languages, DevOps


class TechnologiesState(rx.State):
    user_filter: str = ""
    langs: list[dict[str, str]] = [item for item in Languages.items.value.values()]
    devops: list[dict[str, str]] = [item for item in DevOps.items.value.values()]

    @rx.var
    def selected(self) -> dict:
        requested = self.router.page.params.get("technology")
        data = {}
        data.update(Languages.items.value)
        data.update(DevOps.items.value)
        return data.get(requested)

    def set_technologies(self, value: str):
        self.user_filter = value
        self.langs = [
            item
            for item in Languages.items.value.values()
            if value.lower() in item["title"].lower()
        ]
        self.devops = [
            item
            for item in DevOps.items.value.values()
            if value.lower() in item["title"].lower()
        ]
