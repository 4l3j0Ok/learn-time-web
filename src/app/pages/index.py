import reflex as rx
from app.views.index import view
from app.styles.common import ANIMATIONS


@rx.page("/", title="Learn Time by Alejoide")
def index() -> rx.Component:
    return rx.container(view(), class_name=ANIMATIONS.get("zoom_in"))
