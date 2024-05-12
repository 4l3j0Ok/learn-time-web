import reflex as rx
from app.views.header import header
from app.views.technologies import langs, devops, more_soon
from app.views.footer import footer


@rx.page("/", title="Learn Time by Alejoide")
def index() -> rx.Component:
    return (
        header(),
        langs(),
        devops(),
        more_soon(),
        footer(),
    )
