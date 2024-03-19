"""Serves as a proxy to retrieve the info about the articles and reviews."""
from action_photo_passion import cache

class ServiceArticleReader:
    """proxy to retrieve the info"""

    cache_name:str = "article_cache"

    articles:list = []

    # Setting for mock
    is_simulation:bool = True

    def __init_cache(self):
        cache.add_target_cache_to_cache_inventory(self.cache_name)

    def __has_cache_dicrepencies(self,cache_article:list,payload_article:list) -> dict:
        new_cache:list = cache_article
        
        if len(payload_menu_items) != len(cache_menu):
            new_cache = [set(cache.__retrieve_cache__(self.cache_name)).union(set(payload_menu_items))]

        return {"status":True, "new_cache":new_cache}


    def __update_cache(self,menu_items:list):
        if len(cache.__retrieve_cache__(self.cache_name)) <= 0:
            cache[self.cache_name] = [item for item in menu_items]
        elif len(cache.__retrieve_cache__(self.cache_name)) != len(menu_items):
            set_for_cache = set()
    
    def get_payload_all_reviews(self) -> None:
        self.__init_cache()

        articles = [
            dict(id=1,title="test 1",description="description test 1"),
            dict(id=2,title="test 2",description="description test 2"),
            dict(id=3,title="test 3",description="description test 3"),
        ]
        for article in articles:
            cache.add_to_cach(ArticleParser(**article))


    def get_payload_review(self,article_id:int) -> "ObjectParser":
        if cache.exists_in_cache("cache_article", article_id):
            return cache.get_from_cache("cache_article",article_id)
        else:
            return None 


