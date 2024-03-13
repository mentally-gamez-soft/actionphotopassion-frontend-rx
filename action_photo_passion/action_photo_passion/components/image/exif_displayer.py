import reflex as rx

def display_exif() -> rx.Component:
    return rx.vstack(
            rx.heading("Train the AI model."), 
            width="100%"
    )