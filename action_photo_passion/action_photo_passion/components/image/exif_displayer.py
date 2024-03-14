"""Represents the component to display the exifs of an image."""

import reflex as rx


def display_exif() -> rx.Component:
    """Display the exifs of an image.

    Returns:
        rx.Component: A component from a reflex/react/vuejs perspective.
    """
    return rx.vstack(rx.heading("Train the AI model."), width="100%")
