"""Serves as a proxy to retrieve the information about an image."""

from action_photo_passion import cache
from action_photo_passion.helpers.image_parser import ImageParser


class ServiceImageReader:
    """Proxy to retrieve the information."""
    def get_payload_all_images(self) -> None:
        self.__init_cache()

        images = [
            {"id": 1,
            "title": "Almudena in Madrid",
            "description": "A superb church in the heart of Madrid",
            "gps-altitude": 0.1254,
            "fstop": 16,
            "flash": 1,
            "gps-longitude": 1.1245,
            "gps-latitude": 0.8754,
            "date-document": "2024-01-01 10:02:09",
            "date-edit": "2024-01-05 18:35:09",
            "camera-model": "Sony A58 SLTA58",
            "camera-manufacturer": "Sony",
            "focal-length": "65mm",
            "iso": "100",
            "exposure-time": "235",
            "lens-model": "Tamron A035",
            "lens-manufacturer": "Tamron",
            "exif-version": "0230",
            "url-image-source": "https://actionphotopassion.com/media/gallery/Churches/public/web_almundena_002.jpg_810w.jpg",
            },
            {"id": 2,
            "title": "Abarth 2",
            "description": "124 spider",
            "gps-altitude": 0.1254,
            "fstop": 5.6,
            "flash": 0,
            "gps-longitude": 1.1245,
            "gps-latitude": 0.8754,
            "date-document": "2022-10-09 11:02:09",
            "date-edit": "2023-06-05 09:35:09",
            "camera-model": "Sony A7 ILCE7",
            "camera-manufacturer": "Sony",
            "focal-length": "135mm",
            "iso": "500",
            "exposure-time": "235",
            "lens-model": "Tamron A035",
            "lens-manufacturer": "Tamron",
            "exif-version": "0230",
            "url-image-source": "https://actionphotopassion.com/media/gallery/Churches/public/web_almundena_002.jpg_810w.jpg",
            },
        ]
        for image in images:
            cache.add_to_cache(ImageParser(**image))

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
