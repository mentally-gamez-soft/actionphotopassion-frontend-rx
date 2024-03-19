"""Serves as a proxy to retrieve the information for the different menus."""

from action_photo_passion import cache

class ServiceMenuReader:
    """Proxy to retrieve the information."""

    cache_name:str = "menu_cache"

    menus:list = []

    # Setting for mock
    is_simulation:bool = True

    def __init_cache(self):
        cache.add_target_cache_to_cache_inventory(self.cache_name)

    def __has_cache_dicrepencies(self,cache_menu:list,payload_menu_items:list) -> dict:
        new_cache:list = cache_menu
        
        if len(payload_menu_items) != len(cache_menu):
            new_cache = [set(cache.__retrieve_cache__(self.cache_name)).union(set(payload_menu_items))]

        return {"status":True, "new_cache":new_cache}


    def __update_cache(self,menu_items:list):
        if len(cache.__retrieve_cache__(self.cache_name)) <= 0:
            cache[self.cache_name] = [item for item in menu_items]
        elif len(cache.__retrieve_cache__(self.cache_name)) != len(menu_items):
            set_for_cache = set()
            
        


    def get_payload_menus(self) -> list:
        """Get the menus information from web service all.
        """

        self.__init_cache()

        if self.is_simulation:
            self.set_mocked_menus()
        else:
            self.__call_ws_menu_item()

            #ajouter dan le cache les menu items




    def get_number_menu_items(self):
        return len(self.menus)

    def get_menu_item(self,id:int) -> dict:
        list_item = filter(lambda x: x["id"] == id, self.menus)

        return list_item[0] if list_item else None

    def get_menu_icon(self, id:int) -> str:
        menu_item = self.get_menu_item(id)

        if menu_item:
            return menu_item.get("icon")

        return None

    def get_menu_header(self, id:int) -> str:
        menu_item = self.get_menu_item(id)

        if menu_item:
            return menu_item.get("header")

        return None
    
    def get_menu_description(self, id:int) -> str:
        menu_item = self.get_menu_item(id)

        if menu_item:
            return menu_item.get("description")

        return None
    