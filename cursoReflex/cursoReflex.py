import reflex as rx
from cursoReflex.components.navbar import navbar
from cursoReflex.components.footer import pie
from cursoReflex.views.header.header import header
from cursoReflex.views.links.links import links

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        pie()
    )


app = rx.App()
app.add_page(index)
app.compile()