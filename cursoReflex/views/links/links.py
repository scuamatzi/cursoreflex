import reflex as rx
from cursoReflex.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "http://google.com"),
        link_button("Youtube", "http://google.com"),
        link_button("TikTok", "http://google.com")
    )