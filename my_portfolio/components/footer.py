import reflex as rx
from my_portfolio.styles.styles import Size as Size
import datetime

GITHUB_URL = "https://github.com/JesusdDev"

def footer() -> rx.Component:
    return rx.stack(
            rx.link(f"{datetime.date.today().year} Portolio Interactivo v1 Building software",
                href=GITHUB_URL,
                is_external=True
            ),
            rx.text(
                "from Maracaibo to the World.".upper(),
                margin_top="0px !important"
            ),        
    margin_botom=Size.BIG.value,
    )


