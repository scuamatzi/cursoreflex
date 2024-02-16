import reflex as rx
import datetime

def pie() -> rx.Component:
    return rx.vstack(
        rx.image(src="logo.png"),
        rx.link(
            f"@scuamatzi {datetime.date.today().year}",
            href="http://salvadorcuamatzi.pro",
            is_external=True
        ),
        rx.text("Sysadmin, DevOps, Python Dev, Blender.")
    )