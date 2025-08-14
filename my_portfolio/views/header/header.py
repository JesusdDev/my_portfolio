import reflex as rx
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.styles import Spacing as Spacing
from my_portfolio.styles.colors import Color, TextColor


def header() -> rx.Component:
    return rx.stack(
        rx.hstack(
            rx.avatar(src="Perfil1.jpg",size="7"),
            rx.heading("Hola, mi nombre es", color=TextColor.SECONDARY.value),
            rx.heading("Jesus Peña", color=TextColor.PRIMARY.value),
            align="center"                        
        ),
        rx.vstack(
            rx.text("""Con más de 7 años de trayectoria como Ingeniero de Sistemas, 
                    mi pasión es potenciar negocios. Ofrezco servicios freelance en 
                    desarrollo web (Python FullStack), automatización de procesos y 
                    análisis de datos para emprendedores y startups que buscan escalar."""
            ),
        ),
        direction="column"
    )
    