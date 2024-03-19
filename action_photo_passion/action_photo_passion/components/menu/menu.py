import reflex as rx



"""Represents the component to display the exifs of an image."""

import reflex as rx
from action_photo_passion.states.menus import MenuState


def menu_item() -> rx.Component:
    """Display the an item of the menu bar.

    Returns:
        rx.Component: A component from a reflex/react/vuejs perspective.
    """
    return rx.vstack(
        rx.card(
            rx.avatar(src=MenuState.icon),
            rx.heading(MenuState.header),
            rx.text(MenuState.desc)
        ),
        as_child = True
    )
