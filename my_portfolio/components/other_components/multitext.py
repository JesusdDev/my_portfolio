import reflex as rx

class Multilingualstate(rx.State):
    texts = [
        "Desarrollador Full Stack.",
        "Full Stack Developer.",
        "Développeur Full Stack.",
        "Desenvolvedor Full Stack."
    ]
    text_index: int = 0

    def next_text(self):
        self.text_index = (self.text_index +1) % len(self.texts)

def multileng_text_component() -> rx.Component:
    #Componente para cambiar de texto cada 3 segundos
    return rx.text(
        Multilingualstate.texts[Multilingualstate.text_index],
        color="#a9b1d6",  # Color de texto principal de Tokyo Night
        font_size="1em",
        margin_top="0.5em",
        #rx.moment(interval=3000),
    )
        
    