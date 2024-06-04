import reflex as rx
from app.modules.constants import Languages, DevOps
from typing import Union, List, Dict


class TechnologyType(rx.Base):
    title: str
    content: str
    icon: str
    page: str
    docs_url: str
    courses: List[Dict[str, Union[str, bool]]]
    resources: List[Dict[str, str]]


class TechnologiesState(rx.State):
    user_filter: str = ""
    langs: List[TechnologyType] = [item for item in Languages.items.value.values()]
    devops: List[TechnologyType] = [item for item in DevOps.items.value.values()]

    @rx.var
    def selected(self) -> TechnologyType:
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
