import unittest

from action_photo_passion import cache
from action_photo_passion.helpers.image_parser import ImageParser


class TestCacheService(unittest.TestCase):
    def setUp(self) -> None:
        image_data = {
            "ID-image": 2,
            "gps-altitude": 0.3562,
            "fstop": 8,
            "flash": 0,
            "gps-longitude": 1.7855,
            "gps-latitude": 0.32554,
            "date-photo": "2022-09-13 13:02:09",
            "date-edit": "2024-10-18 15:35:09",
            "camera-model": "Sony A77 SLTA77",
            "camera-manufacturer": "Sony",
            "focal-length": "85mm",
            "iso": "600",
            "exposure-time": "0.256",
            "lens-model": "Tamron A017",
            "lens-manufacturer": "Tamron",
            "exif-version": "0230",
            "url-image-source": "https://actionphotopassion.com/media/gallery/Travels/public/web_madrid_009.jpg_810w.jpg",
        }
        self.image_parser = ImageParser(**image_data)

    def test_image_not_existing_in_cache(self):
        self.assertFalse(
            cache.exists_image_in_cache(image_reader=self.image_parser),
            "The image should not be in the cache for the moment !!!",
        )

    def test_image_added_to_cache(self):
        cache.add_image_to_cache(self.image_parser)
        self.assertTrue(
            cache.exists_image_in_cache(image_reader=self.image_parser),
            "The image should exist in the cache now !!!",
        )

    def test_id_image_already_existing_in_cache(self):
        cache.add_image_to_cache(self.image_parser)
        self.assertTrue(
            cache.exists_image_id_in_cache(image_id=2)["status"],
            "The image should exist in the cache now !!!",
        )
