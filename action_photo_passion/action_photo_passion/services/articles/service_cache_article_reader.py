"""Defines the service for a cache about the articles read to avoid web calls."""

from action_photo_passion.action_photo_passion.helpers.article_parser import (
    ArticleParser,
)


class ServiceCacheArticleReader:
    """Service provider as a cache for the articles read by user."""

    cache_article: list = []

    def exists_article_id_in_cache(self, article_id: int) -> dict:
        """Check the existence of an article according to its id.

        Args:
            article_id (int): The id of an article.

        Returns:
            dict: status (bool) and article resume (str)
        """
        element = [
            article
            for article in self.cache_article
            if article.get_id_article() == article_id
        ]
        return {"status": len(element) > 0, "article": element[:]}

    def exists_article_in_cache(self, article_reader: ArticleParser) -> bool:
        """Check the validity of an article.

        Args:
            article_reader (ArticleParser): The full article object to verify.

        Returns:
            bool: True if the article is valid.
        """
        element = [
            article
            for article in self.cache_article
            if article.get_id_article() == article_reader.get_id_article()
        ]
        return len(element) > 0

    def add_article_to_cache(self, article_reader: ArticleParser):
        """Add an article to the cache service.

        Args:
            article_reader (ArticleParser): The article to record.
        """
        if not self.exists_article_in_cache(article_reader):
            self.cache_article.append(article_reader)

    def get_article_from_cache(self, article_id: int) -> "ArticleParser":
        """Retrieve an article from the cache service according to its id.

        Args:
            article_id (int): The id of the article.

        Returns:
            ArticleParser: The valid article found in cache.
        """
        res = self.exists_article_id_in_cache(article_id)
        if res["status"]:
            return res["article"]
