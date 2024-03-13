import unittest
from action_photo_passion.helpers.image_parser import ImageParser

class TestImageExifReaderService(unittest.TestCase):
    def setUp(self) -> None:
        self.img  = ImageParser()

    def test_exists_mock_values(self):

        self.assertTrue(self.img.imageExif is not None,"The image is None !!!!")

    
    def test_mock_values_loaded(self):
        self.assertEqual(self.img.get_exif_camera_manufacturer(),'Sony', "The mock data is not loaded !!!!")