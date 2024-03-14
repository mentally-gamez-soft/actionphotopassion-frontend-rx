"""Serves as a super class proxy to decode the content of an object from a webservice call."""

class ObjectParser:
    """Tool to get all the data from an object. This will be an abstract class for the element of the app."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize an instance of ArticleParser."""
        self.data = kwargs
