"""Represents the component to display the details of an image."""

import reflex as rx

from action_photo_passion.states.image_state import ImageState


def display_image() -> rx.Component:
    """Display the detail of an image.

    Returns:
        rx.Component: A component from a reflex/react/vuejs perspective.
    """
    return rx.vstack(
        rx.heading("Display Image here"),
        rx.image(
            src=ImageState.img_str_info["url-image-source"],
            width="100px",
            height="auto",
        ),
        rx.text(ImageState.img_str_info["title"]),
        width="100%",
        # test CZO github
    )
