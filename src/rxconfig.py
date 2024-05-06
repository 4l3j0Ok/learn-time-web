import reflex as rx
import os


config = rx.Config(
    app_name="app",
    cors_allowed_origins=os.environ.get("ALLOWED_ORIGINS", "*").split(","),
)
