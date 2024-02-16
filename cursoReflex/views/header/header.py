import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Salvador Cuamatzi", size="xl"),
        rx.text("@scuamatzi"),
        rx.text("Hola mi nombre es Salvador Cuamatzi"),
        rx.text("Soy Ingeniero Electrónico con más de 15 años como Linux Sysadmin y oriendtado a DevOps")
    )