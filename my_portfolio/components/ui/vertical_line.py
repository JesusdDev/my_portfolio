import reflex as rx

def vertical_line() -> rx.Component:
    return rx.center(
        rx.box(
            width="2px",  # Grosor de la línea
            height="100px",  # Longitud de la línea
            background_color="green",  # Color de la línea
            border_radius="10px" # Opcional: para darle bordes redondeados
        )
    )