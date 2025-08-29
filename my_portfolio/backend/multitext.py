import reflex as rx

class Multilingualstate(rx.State):
    texts = [
        "Desarrollador Full Stack.",
        "Full Stack Developer.",
        "Développeur Full Stack.",
        "Desenvolvedor Full Stack."
    ]
    text_index: int = 0

    @rx.event
    def next_text(self, text_index: int, texts: list):
        self.text_index = (self.text_index +1) % len(self.texts)

def multileng_text_component() -> rx.Component:
    return rx.text(
        Multilingualstate.texts[Multilingualstate.text_index]
    )
        
    