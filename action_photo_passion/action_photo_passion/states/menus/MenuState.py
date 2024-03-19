"""Define the states for the images."""

import reflex as rx
from action_photo_passion.services.menus.service_menus_reader import (
     ServiceMenuReader,
 )


class MenuState(rx.State):
    """State for the menu"""

    menu_icon: str
    menu_header: str
    menu_description:str

    def retrieve_menu(self):
        service_reader = ServiceMenuReader()

        self.menu_icon = service_reader.get_menu_icon()
        self.menu_header = service_reader.get_menu_header()
        self.menu_description = service_reader.get_menu_description
