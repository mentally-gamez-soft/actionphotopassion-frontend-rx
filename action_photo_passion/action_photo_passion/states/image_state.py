from action_photo_passion.helpers.image_parser import ImageParser
from action_photo_passion.services.service_image_details_reader import ServiceImageReader

import reflex  as rx

class ImageState(rx.State):
    
    img_str_info:dict
    img_gps_coordinates: dict
    img_exif_standard_exposure_triangle: dict
    img_exif_flash: str
    img_exif_focal_length: str
    img_dates: dict
    camera_lens_data:dict 
    img_exif_version:str 

    def get_image(self):
        service_reader = ServiceImageReader()
        image = ImageParser(service_reader.get_payload_image(1))
        
        self.img_str_info["ID-image"] = image.get_id_image()
        self.img_str_info["url-image-source"] = image.get_image_url()
        self.img_str_info["title"] = image.get_title_image()
        self.img_str_info["description"] = image.get_description_image()

        self.img_gps_coordinates["gps-latitude"] = image.get_exif_gps_latitude()
        self.img_gps_coordinates["gps-altitude"] = image.get_exif_gps_altitude()
        self.img_gps_coordinates["gps-longitude"] = image.get_exif_gps_longitude()
        
        self.img_exif_standard_exposure_triangle["fstop"] = image.get_exif_fstop()
        self.img_exif_standard_exposure_triangle["iso"] = image.get_exif_iso()
        self.img_exif_standard_exposure_triangle["exposure-time"] = image.get_exif_exposure_time()

        self.img_exif_flash = image.get_exif_flash()

        self.img_dates["date-photo"] = image.get_exif_date_photo_taken()
        self.img_dates["date-edit"] = image.get_exif_date_photo_edit()

        self.camera_lens_data["camera-manufacturer"] = image.get_exif_camera_manufacturer()
        self.camera_lens_data["camera-model"] = image.get_exif_camera_model()
        self.camera_lens_data["lens-manufacturer"] = image.get_exif_lens_manufacturer()
        self.camera_lens_data["lens-model"] = image.get_exif_lens_model()

        self.img_exif_focal_length = image.get_exif_focal_length()
 



