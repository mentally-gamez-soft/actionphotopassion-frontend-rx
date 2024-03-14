"""Serves as a proxy to decode the content of an article from a webservice call."""

class ArticleParser:
    """Tool to get all the data from an article. title, author, resume and more."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize an instance of ArticleParser."""
        self.article_data = kwargs
