"""Serves as a proxy to retrieve the info about the articles and reviews."""
from action_photo_passion import cache

class ServiceArticleReader:
    """proxy to retrieve the info"""

    def get_payload_review(self,review_id:int) -> "ObjectParser":

        if cache.exists_in_cache("cache_article", article_id):
            return cache.get_from_cache("cache_article",artcile_id)
