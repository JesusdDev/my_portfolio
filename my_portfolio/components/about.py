import reflex as rx
from my_portfolio.components.ui.vertical_line import vertical_line
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.colors import Color
from my_portfolio.styles.colors import TextColor
from my_portfolio.styles.styles import Spacing as Spacing

def about() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.heading("$ cat aboutme.txt",
                       padding=Size.SMALL.value
            ),
            rx.text("""Soy un desarrollador full stack apasionado por crear experiencias web 
                    innovadoras y funcionales. Me especializo en tecnologías modernas como React, 
                    Node.js y TypeScript.""",
                    padding_x=Size.DEFAULT.value

            ),
            rx.text("""Con más de 5 años de experiencia en el desarrollo web, 
                    he trabajado en proyectos que van desde aplicaciones empresariales hasta 
                    plataformas de e-commerce, siempre enfocándome en escribir código limpio y 
                    mantenible.""",
                    padding=Size.DEFAULT.value
            ),
            rx.text("""Cuando no estoy programando, me gusta contribuir a proyectos de código abierto, 
                    aprender nuevas tecnologías y compartir conocimiento con la comunidad de desarrolladores.""",
                    padding_x=Size.DEFAULT.value
            ),
            width="100%",
            Spacing=Spacing.VERY_SMALL.value,
            border_width="1px",
            border_radius="30px",
            border_color=Color.BORDER_COLOR.value,
            padding=Size.SMALL.value,
        ),
        rx.box(
            rx.heading("Habilidades Técnicas",
                       padding=Size.SMALL.value
            ),
            rx.flex(
                rx.card("Python", color=TextColor.EXTRA.value, size="1"),
                rx.card("PostgresQL", color=TextColor.EXTRA.value, size="1"),
                rx.card("Git y gitHub", color=TextColor.EXTRA.value, size="1"),
                rx.card("Backend", color=TextColor.EXTRA.value, size="1"),
                rx.card("Frontend con Reflex", color=TextColor.EXTRA.value, size="1"),
                spacing="2",
                align_items="flex-start",
                flex_wrap="wrap",
                padding_x=Size.DEFAULT.value
            ),              
        border_width="1px",
        border_color=Color.BORDER_COLOR.value,
        background_color=Color.SECONDARY_BG.value,
        border_radius="30px",
        width="100",
        justify="center",
        padding=Size.SMALL.value
        ),
        rx.vstack(
            rx.heading("Experiencia Profesional",
                       padding=Size.SMALL.value
            ),
            rx.hstack(
                vertical_line(),
                rx.vstack(
                    rx.text("Senior Departamento de sistemas y fullstack"),
                    rx.text("Farmacias Manriquez"),
                    rx.text("2022 - 2025"),
                    rx.text("Desarrollo de aplicaciones web modernas utilizando React, Node.js y tecnologías cloud."),
                    spacing=Spacing.ZERO.value
                ),
                spacing=Spacing.DEFAULT.value
            ),
            rx.hstack(
                vertical_line(),
                rx.vstack(
                    rx.text("Analista de Sistemas"),
                    rx.text("O´mas Ltda"),
                    rx.text("2020 - 2022"),
                    rx.text("Desarrollo de aplicaciones web modernas utilizando React, Node.js y tecnologías cloud."),
                    spacing=Spacing.ZERO.value
                ),
                spacing=Spacing.DEFAULT.value
            ),
            rx.hstack(
                vertical_line(),
                rx.vstack(
                    rx.text("Junior Developer"),
                    rx.text("Bizmind"),
                    rx.text("2019 - 2020"),
                    rx.text("Desarrollo de aplicaciones web modernas utilizando React, Node.js y tecnologías cloud."),
                    spacing=Spacing.ZERO.value
                ),
                spacing=Spacing.DEFAULT.value
            ),              
            border_width="1px",
            border_color=Color.BORDER_COLOR.value,
            background_color=Color.SECONDARY_BG.value,
            border_radius="30px",
            width="100",
            justify="center",
            padding=Size.SMALL.value
        ),        
        padding=Size.DEFAULT.value,        
        width="100%",
        height="auto",
        direction="column",
        align="center",
        border_width="1px",
        border_radius="30px",
        border_color=Color.BORDER_COLOR.value,
        spacing=Spacing.DEFAULT.value,
        background_color=Color.SECONDARY_BG.value
    )