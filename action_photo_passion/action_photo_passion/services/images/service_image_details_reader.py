from action_photo_passion import cache
from action_photo_passion.helpers.image_parser import ImageParser

class ServiceImageReader:

    def get_payload_image(self,image_id:int) -> dict:
        if cache.exists_image_in_cache(image_id):
            return cache.get_image_from_cache(image_id=image_id)
        return ImageParser()