"""Represents the component for the headline of an article."""

import reflex as rx

from action_photo_passion.states.image_state import ImageState


def display_image() -> rx.Component:
    """Represent the component for displaying the headlines of an article."""
    return rx.vstack(
        rx.heading("Display Image here"),
        rx.image(
            src=ImageState.img_str_info["url-image-source"],
            width="100px",
            height="auto",
        ),
        rx.text(ImageState.img_str_info["title"]),
        width="100%",
    )
