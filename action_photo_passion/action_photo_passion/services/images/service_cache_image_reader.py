from action_photo_passion.helpers.image_parser import ImageParser

class ServiceCacheImageReader:

    cache_image:list = [] 
    
    def exists_image_id_in_cache(self, image_id:int) -> dict:
        element = [img for img in self.cache_image if img.get_id_image() == image_id]
        return {"status":len(element) > 0, "image":element[:]}
    
    def exists_image_in_cache(self, image_reader:ImageParser) -> bool:
        element = [img for img in self.cache_image if img.get_id_image() == image_reader.get_id_image()]
        return len(element) > 0

    def add_image_to_cache(self, image_reader:ImageParser):
        if not self.exists_image_in_cache(image_reader):
            self.cache_image.append(image_reader)

    def get_image_from_cache(self, image_id:int):
        res = self.exists_image_id_in_cache(image_id)
        if res["status"]:
            return res["image"]
