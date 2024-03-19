from action_photo_passion.helpers.object_parser import ObjectParser

class MenuParser(ObjectParser):

    def set_mocked_menus(self):
        menus = [
            {
                "id":1,
                "icon":"portfolio.png",
                "title":"Show The Art Book",
                "descrition":"Art Gallery"
            },
            {
                "id":2,
                "icon":"reviews.png",
                "title":"Reviews and Blogs",
                "description":"The best art curated reviews."
            },
            {
                "id":3,
                "icon":"prints.png",
                "title":"Collectibles and Prints",
                "description":"Don't be shy and give yourself a special treat."
            },
            {
                "id":4,
                "icon":"job.png",
                "title":"Book a meeting",
                "description":"Need insights and guidance, let's meet."
            },
            {
                "id":5,
                "icon":"about.png",
                "title":"About the artist",
                "description":"Who am I, what I do, What I like."
            },
        ]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def get_header(self):
        """Get the title of one menu item.

        Returns:
            str: the title for 1 menu item.
        """
        return self.get_title()

    def get_description(self):
        """Get the description of 1 menu item.

        Returns:
            str: the description of 1 menu item.
        """
        return self.get_description()

    def get_menu_id(self) -> int:
        """Get the id for 1 menu item.
    
        Returns:
            int: the id of 1 menu item.
        """
        return self.get_id()

    def get_menu_icon(self) -> str:
        """Get the path to the image icon of 1 menu item.
    
        Returns:
            int: the path to the image icon of 1 menu item.
        """
        return self.data.get("icon")