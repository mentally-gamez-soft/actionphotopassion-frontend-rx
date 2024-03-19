import unittest
from action_photo_passion import cache

class TestCacheManagerInventory(unittest.TestCase):

    def setUp(self):
        self.cache_name_test = "cache_menu"
        cache.add_target_cache_to_cache_inventory(cache_key=self.cache_name_test)

        img_mock = {"id": 2,
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
            }

    def tearDown(self):
        pass 

    def test_add_cache_to_inventory_manager(self):
        self.assertEqual(cache.__retrieve_cache__(cache_key=self.cache_name_test),
                            [],
                            "The cache menu has not been added !!!")

    def test_no_cache_in_inventory_manager(self):
        self.assertEqual(cache.__retrieve_cache__(cache_key="not-existing-cache"),
                            None,
                            "The cache shouldn't exist here !!!")

    def test_delete_cache_from_inventory_manager(self):
        cache.delete_target_cache_from_cache_inventory(self.cache_name_test)

        self.assertEqual(cache.__retrieve_cache__(cache_key=self.cache_name_test),
                         None,
                         "The cache menu has not been deleted !!!")

    def exist_cache_in_manager(self):
        pass 

    
    