import reflex as rx

#Común
"""
Aquí colocaré una imagen en su momento
y la Información de metadata
"""
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

_meta =  [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": "preview"},
]

#index

index_tittle = "MyPortfolio"
index_description = "Aquí encontraras mis proyectos e información profesional"

index_meta = [
    {"name": "og:tittle", "content": index_tittle},
    {"name": "og:description", "content": index_description}
]

index_meta.extend(_meta)

#about

about_tittle = "MyPortfolio"
about_description = "Aquí encontraras mis proyectos e información profesional"

about_meta = [
    {"name": "og:tittle", "content": about_tittle},
    {"name": "og:description", "content": about_description}
]

about_meta.extend(_meta)

#projects

projects_tittle = "MyPortfolio"
projects_description = "Aquí encontraras mis proyectos e información profesional"

projects_meta = [
    {"name": "og:tittle", "content": projects_tittle},
    {"name": "og:description", "content": projects_description}
]

projects_meta.extend(_meta)

#contact

contact_tittle = "MyPortfolio"
contact_description = "Aquí encontraras mis proyectos e información profesional"

contact_meta = [
    {"name": "og:tittle", "content": contact_tittle},
    {"name": "og:description", "content": contact_description}
]

contact_meta.extend(_meta)

