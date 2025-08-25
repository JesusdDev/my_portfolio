import reflex as rx
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.styles import Spacing as Spacing
from my_portfolio.styles.colors import Color
from my_portfolio.styles.colors import TextColor

def home() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.heading("🚀 Explora mi trabajo usando comandos de terminal o los botones de navegación", padding=Size.SMALL.value, align="center"),
            rx.text("$Whoami", align="center", color=TextColor.EXTRA.value),
            rx.text("FullStack Python", align="center"),            
            rx.text("$ echo 'Especialidades'", align="center"),
            rx.box(
                rx.stack(rx.text("Data Science •", color=TextColor.EXTRA.value),
                    rx.text("Process Automation •", color=TextColor.EXTRA.value),
                    rx.text("Desktop Applications", color=TextColor.EXTRA.value),
                    spacing="1",
                    direction="row",
                    justify="center"
                )                                                            
            ),
            border_width="1px",
            border_color=Color.BORDER_COLOR.value,
            background_color=Color.SECONDARY_BG.value,
            border_radius="30px",
            width="100%",
            justify="center",
            padding=Size.SMALL.value   
        ),
        rx.box(
            rx.heading("Navegación",padding=Size.SMALL.value, align="center"),
            rx.hstack(
                rx.box(                  
                    rx.text("Comandos Terminal: ", color=TextColor.EXTRA.value),
                    rx.text("• Cd projects - Ir a proyectos "),
                    rx.text("• Cd .. - Retroceder "),
                    rx.text("• Ls - Listar archivos"),
                    rx.text("• Cat aboutme.txt - Ver biografia"),
                    flex_grow=1,
                    text_align="left"
                ),
                rx.box(
                    rx.text("Navegación Visual:", color=TextColor.EXTRA.value),
                    rx.text("• Usa los botones de arriba"),
                    rx.text("• Breadcrumbs clicleables"),
                    rx.text("• Navegación intuitiva"),
                    rx.text("• Compatible con ambos métodos"),
                    flex_grow=1,
                    text_align="end"
                )               
            ),
        border_width="1px",
        border_color=Color.BORDER_COLOR.value,
        background_color=Color.SECONDARY_BG.value,
        border_radius="30px",
        width="100%",
        justify="center",
        padding=Size.SMALL.value
        ),
        rx.box(
            rx.heading("Comandos Avanzados", padding=Size.SMALL.value, align="center"),
            rx.hstack(
                rx.box(
                    rx.text("• Cd projects/ecommerce-platform"),
                    rx.text("• Ls projects"),
                    rx.text("• Contact --email"),
                    rx.text("• Help"),
                    flex_grow=1,
                    text_align="start"
                ),
                rx.box(
                    rx.text("• Ver proyectos especificos"),
                    rx.text("• Listar todos los proyectos"),
                    rx.text("• Abrir formulario de contacto"),
                    rx.text("• Ver todos los comandos"),
                    flex_grow=1,
                    text_align="end"
                )                                                              
            ),
            border_width="1px",
            border_color=Color.BORDER_COLOR.value,
            background_color=Color.SECONDARY_BG.value,
            border_radius="30px",
            width="100%",
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