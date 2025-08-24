import reflex as rx
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.colors import Color
from my_portfolio.styles.colors import TextColor
from my_portfolio.styles.styles import Spacing as Spacing

def contact() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.heading("$ contact --email",
                       padding_top=Size.SMALL.value,
                       padding_x=Size.DEFAULT.value
            ),
            rx.text("""Iniciando formulario de contacto... 
                    ¡Hablemos de tu próximo proyecto!""",
                    padding_bottom=Size.DEFAULT.value,
                    padding_x=Size.DEFAULT.value
            ),
            width="100%",
            Spacing=Spacing.VERY_SMALL.value,
            border_width="1px",
            border_radius="30px",
            border_color=Color.BORDER_COLOR.value,
            margin=Size.SMALL.value,
            padding=Size.SMALL.value,
        ),
        #Contenedor de formulario e información
        rx.hstack(
            rx.stack(
                rx.box(
                    rx.heading("Envíame un mensaje", size="2"),                
                # Formulario
                    rx.box(
                    rx.input(placeholder="Tu nombre"),
                    rx.input(placeholder="Tu correo"),
                    rx.input(placeholder="Asunto"),
                    rx.text_area(placeholder="Tu mensaje"),
                    rx.button("Enviar", width="100%")                    
                    ),
                    width="100%",
                    padding=Size.DEFAULT.value,
                    border_width="1px",
                    border_radius="30px",
                    border_color=Color.BORDER_COLOR.value,
                    spacing=Spacing.SMALL.value,
                    background_color=Color.SECONDARY_BG.value,
                    direction="column",
                ),
                justify="start",
                width="100%"
            ),                
            rx.stack(
                rx.box(
                    rx.heading("Información de Contacto", size="2"),
                    rx.hstack(
                        rx.image("icons/mail.svg",
                                 width="30px",
                                 height="auto",                                
                                 ),
                        rx.vstack(
                            rx.text("Email"),
                            rx.link(rx.text("contacto@ejemplo.com", color=TextColor.EXTRA.value)),
                            margin=Size.ZERO.value,
                            spacing=Spacing.ZERO.value
                        )
                    ),
                    rx.hstack(
                        rx.image("icons/phone.svg",
                                 width="30px",
                                 height="auto",                              
                                 ),
                        rx.vstack(
                            rx.text("Teléfono"),
                            rx.link(rx.text("+56 9 3018 7627", color=TextColor.EXTRA.value)),
                            margin=Size.ZERO.value,
                            spacing=Spacing.ZERO.value
                        )                        
                    ),
                    rx.hstack(
                        rx.image("icons/map-pin-house.svg",
                                 width="30px",
                                 height="auto",                                 
                                 ),
                        rx.vstack(
                            rx.text("Ubicación"),
                            rx.link(rx.text("Santiago de Chile", color=TextColor.EXTRA.value)),
                            margin=Size.ZERO.value,
                            spacing=Spacing.ZERO.value
                        )
                    ),
                    #width="100%",
                    padding=Size.DEFAULT.value,
                    border_width="1px",
                    border_radius="30px",
                    border_color=Color.BORDER_COLOR.value,
                    spacing=Spacing.SMALL.value,
                    background_color=Color.SECONDARY_BG.value
                ),
                rx.box(
                    rx.heading("Sigue mi trabajo en", size="2"),
                    rx.link(
                        rx.hstack(
                            rx.image("icons/github.svg"),
                            rx.image("icons/linkedin.svg"),
                            rx.image("icons/twitter.svg"),
                            spacing=Spacing.LARGE.value,
                            width="100%"
                        )
                    ),
                    padding=Size.DEFAULT.value,
                    #width="100%",
                    border_width="1px",
                    border_radius="30px",
                    border_color=Color.BORDER_COLOR.value,
                    background_color=Color.SECONDARY_BG.value
                ),
                rx.box(
                    rx.heading("Disponibilidad", size="2"),
                    rx.text("Disponible para proyectos"),
                    rx.text("Respondo emails en menos de 24 horas"),
                    rx.text("Horario: Lun-Vie 9:00-18:00 CET"),
                    #width="100%",
                    spacing=Spacing.SMALL.value,
                    padding=Size.DEFAULT.value,
                    border_width="1px",
                    border_radius="30px",
                    border_color=Color.BORDER_COLOR.value,
                    background_color=Color.SECONDARY_BG.value
                ),
                width="100%",
                justify="end",
                spacing=Spacing.DEFAULT.value,
                direction="column",
            ),
            spacing="5"
        ),
        padding=Size.DEFAULT.value,        
        width="70%",
        height="auto",
        direction="column",
        align="center",
        border_width="1px",
        border_radius="30px",
        border_color=Color.BORDER_COLOR.value,
        spacing=Spacing.DEFAULT.value,
        background_color=Color.SECONDARY_BG.value
    )