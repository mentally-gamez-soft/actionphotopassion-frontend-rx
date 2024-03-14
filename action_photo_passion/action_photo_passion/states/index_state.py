"""Define the states for the index page."""

import reflex as rx


class ImageState(rx.State):
    """State for the index page."""

    inventory: list = [
        "page_1",
        "page_2",
        "page_3",
    ]
