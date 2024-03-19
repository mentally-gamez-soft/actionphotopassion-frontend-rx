"""Serves as a proxy to decode the content of an article from a webservice call."""

from object_parser import ObjectParser

mock_data = {
    "id": 1,
    "title": "Almudena in Madrid",
    "description": "A superb church in the heart of Madrid",
    "date-document": "2024-01-01 10:02:09",
    "slug": "almudena-in-madrid",
    "url-image-source": "https://actionphotopassion.com/media/gallery/Churches/public/web_almundena_002.jpg_810w.jpg",
}

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

    def get_date_article(self):
        """Get the date the article was written.
    
        Returns:
            int: the id of the article.
        """
        return self.get_date()

    def get_slug_article(self):
        return self.data.get("slug")

    def get_image(self):
        return self.data.get("url-image-source")        