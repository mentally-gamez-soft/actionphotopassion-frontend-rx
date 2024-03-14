"""Serves as a proxy to retrieve the information about an image."""

from action_photo_passion import cache
from action_photo_passion.helpers.image_parser import ImageParser


class ServiceImageReader:
    """Proxy to retrieve the information."""

    def get_payload_image(self, image_id: int) -> "ImageParser":
        """Get the image information from web service all.

        Args:
            image_id (int): the id of an image.

        Returns:
            ImageParser: The image instance.
        """
        if cache.exists_image_in_cache(image_id):
            return cache.get_image_from_cache(image_id=image_id)
        return ImageParser()
