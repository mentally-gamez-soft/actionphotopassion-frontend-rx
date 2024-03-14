"""Defines the service for a cache about the images, to avoid web calls."""

from action_photo_passion.helpers.image_parser import ImageParser


class ServiceCacheImageReader:
    """Service provider as a cache for the images consulted by user."""

    cache_image: list = []

    def exists_image_id_in_cache(self, image_id: int) -> dict:
        """Check the existence of an image according to its id.

        Args:
            image_id (int): The id of the image.

        Returns:
            dict: status (bool) and image.
        """
        element = [
            img for img in self.cache_image if img.get_id_image() == image_id
        ]
        return {"status": len(element) > 0, "image": element[:]}

    def exists_image_in_cache(self, image_reader: ImageParser) -> bool:
        """Check the validity of an image.

        Args:
            image_reader (ImageParser): The full image object to verify.

        Returns:
            bool: True if the image is valid.
        """
        element = [
            img
            for img in self.cache_image
            if img.get_id_image() == image_reader.get_id_image()
        ]
        return len(element) > 0

    def add_image_to_cache(self, image_reader: ImageParser):
        """Add an image to the cache service.

        Args:
            image_reader (ImageParser): The image to save in cache..
        """
        if not self.exists_image_in_cache(image_reader):
            self.cache_image.append(image_reader)

    def get_image_from_cache(self, image_id: int) -> "ImageParser":
        """Retrieve an image from the cache service according to its id.

        Args:
            image_id (int): The id of the image.

        Returns:
            ImageParser: The valid image found in cache.
        """
        res = self.exists_image_id_in_cache(image_id)
        if res["status"]:
            return res["image"]
