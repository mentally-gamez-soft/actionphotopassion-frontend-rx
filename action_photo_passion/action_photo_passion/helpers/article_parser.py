"""Serves as a proxy to decode the content of an article from a webservice call."""

from object_parser import ObjectParser

class ArticleParser(ObjectParser):
    """Tool to get all the data from an article. title, author, resume and more."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize an instance of ArticleParser."""
        super().__init__(*args, **kwargs)

    def get_title_article(self):
        """Get the title of an article.

        Returns:
            str: the title of the article.
        """
        return self.get_title()

    def get_description_article(self):
        """Get the description of an article.

        Returns:
            str: the description of the article.
        """
        return self.get_description()

    def get_id_article(self):
        """Get the id of an article.
    
        Returns:
            int: the id of the article.
        """
        return self.get_id()