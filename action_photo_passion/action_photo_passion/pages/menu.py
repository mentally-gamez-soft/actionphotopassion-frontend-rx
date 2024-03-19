from action_photo_passion.components.menu.menu import menu_item
from action_photo_passion.states.menus import MenuState

@rx.page(route="/", title="Index", on_load=MenuState.get_menu_list)
def menu_items_page() -> rx.Component:
    return rx.vstack(menu_item())