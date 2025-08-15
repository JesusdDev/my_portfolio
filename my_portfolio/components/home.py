import reflex as rx
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.styles import Spacing as Spacing
from my_portfolio.styles.colors import Color
from my_portfolio.styles.colors import TextColor

def home() -> rx.Component:
    return rx.stack(
        rx.box(
            rx.heading("🚀 Explora mi trabajo usando comandos de terminal o los botones de navegación", margin=Size.SMALL.value, align="center"),
            rx.text("$Whoami", align="center", color=TextColor.EXTRA.value),
            rx.text("FullStack Python", align="center"),            
            rx.text("$ echo 'Especialidades'", align="center"),
            rx.text(
                rx.stack(rx.text("Data Science •", color=TextColor.EXTRA.value),
                    rx.text("Process Automation •", color=TextColor.EXTRA.value),
                    rx.text("Desktop Applications", color=TextColor.EXTRA.value),
                    margin=Size.SMALL.value,
                    spacing="1",
                    direction="row",
                    justify="center",
                ),                                                            
            ),
            border_width="1px",
            border_color="#1dd34a",
            background_color=Color.SECONDARY_BG.value,
            border_radius="30px",
            width="90%",
            justify="center",
            margin_top=Size.BIG.value,
            padding=Size.SMALL.value   
        ),
        rx.box(
            rx.heading("Navegación", margin=Size.SMALL.value, align="center"),
            rx.hstack(
                rx.box(                  
                    rx.text("Comandos Terminal: ", color=TextColor.EXTRA.value),
                    rx.text("• Cd projects - Ir a proyectos "),
                    rx.text("• Cd .. - Retroceder "),
                    rx.text("• Ls - Listar archivos"),
                    rx.text("• Cat aboutme.txt - Ver biografia"),
                    flex_grow=1,
                    text_align="left",
                ),
                rx.box(
                    rx.text("Navegación Visual:", color=TextColor.EXTRA.value),
                    rx.text("• Usa los botones de arriba"),
                    rx.text("• Breadcrumbs clicleables"),
                    rx.text("• Navegación intuitiva"),
                    rx.text("• Compatible con ambos métodos"),
                    flex_grow=1,
                    text_align="end",
                ),
            margin=Size.SMALL.value               
            ),
        border_width="1px",
        border_color="#1dd34a",
        background_color=Color.SECONDARY_BG.value,
        border_radius="30px",
        width="90%",
        justify="center",
        padding=Size.SMALL.value
        ),
        rx.box(
            rx.heading("Comandos Avanzados",margin=Size.SMALL.value, align="center"),
            rx.hstack(
                rx.box(
                    rx.text("• Cd projects/ecommerce-platform"),
                    rx.text("• Ls projects"),
                    rx.text("• Contact --email"),
                    rx.text("• Help"),
                    text_align="start",
                ),
                rx.box(
                    rx.text("• Ver proyectos especificos"),
                    rx.text("• Listar todos los proyectos"),
                    rx.text("• Abrir formulario de contacto"),
                    rx.text("• Ver todos los comandos"),
                    flex_grow=1,
                    text_align="end",
                ),
            margin=Size.SMALL.value                                                              
            ),
        border_width="1px",
        border_color="#1dd34a",
        background_color=Color.SECONDARY_BG.value,
        border_radius="30px",
        width="90%",
        justify="center",
        margin_bottom=Size.BIG.value,
        padding=Size.SMALL.value                    
        ),
    width="50%",
    height="auto",
    direction="column",
    align="center",
    border_width="1px",
    border_radius="30px",
    border_color="#1dd34a",
    spacing=Spacing.SMALL.value,
    background_color=Color.SECONDARY_BG.value 
    )