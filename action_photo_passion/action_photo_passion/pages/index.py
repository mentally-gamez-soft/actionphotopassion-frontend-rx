"""Define the index page of the application."""

import reflex as rx

from action_photo_passion.components.image.details.image_displayer import (
    display_image,
)
from action_photo_passion.states.image_state import ImageState


@rx.page(route="/", title="Index", on_load=ImageState.get_image)
def index() -> rx.Component:
    """Display the landing page.

    Returns:
        rx.Component: A component from a reflex/react/vuejs perspective.
    """
    return rx.vstack(display_image())


# @rx.page(route="/img", title="Index")
# def image_page() -> rx.Component:
#     return rx.vstack(
#         rx.container(
#             display_image()
#         )
#     )
