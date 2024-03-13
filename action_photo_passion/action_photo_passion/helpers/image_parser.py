mock_data = {"ID-image":1,
             "title":"Almudena in Madrid",
             "description":"A superb church in the heart of Madrid",
             "gps-altitude":0.1254,
             "fstop":16,
             "flash":1,
             "gps-longitude":1.1245,
             "gps-latitude":0.8754,
             "date-photo":"2024-01-01 10:02:09",
             "date-edit":"2024-01-05 18:35:09",
             "camera-model":"Sony A58 SLTA58",
             "camera-manufacturer":"Sony",
             "focal-length":"65mm",
             "iso":"100",
             "exposure-time":"235",
             "lens-model":"Tamron A035",
             "lens-manufacturer":"Tamron",
             "exif-version":"0230",
             "url-image-source":"https://actionphotopassion.com/media/gallery/Churches/public/web_almundena_002.jpg_810w.jpg"
             }


class ImageParser:
    def __init__(self,*args,**kwargs) -> None:
        self.imageExif = kwargs

    def get_title_image(self):
        if self.imageExif:
            return self.imageExif.get("title",mock_data["title"])
        return mock_data["title"]
    
    def get_description_image(self):
        if self.imageExif:
            return self.imageExif.get("description",mock_data["description"])
        return mock_data["description"]
    
    def get_id_image(self):
        if self.imageExif:
            return self.imageExif.get("ID-image",mock_data["ID-image"])
        return mock_data["ID-image"]
    
    def get_image_url(self):
        if self.imageExif:
            return self.imageExif.get("url-image-source",mock_data["url-image-source"])
        return mock_data["url-image-source"]

    def get_exif_version(self):
        if self.imageExif:
            return self.imageExif.get("exif-version",mock_data["exif-version"])
        return mock_data["exif-version"]

    def get_exif_date_photo_taken(self):
        if self.imageExif:
            return self.imageExif.get("date-photo",mock_data["date-photo"])
        return mock_data["date-photo"]
    
    def get_exif_date_photo_edit(self):
        if self.imageExif:
            return self.imageExif.get("date-edit",mock_data["date-edit"])
        return mock_data["date-edit"]
    
    def get_exif_lens_manufacturer(self):
        if self.imageExif:
            return self.imageExif.get("lens-manufacturer",mock_data["lens-manufacturer"]) 
        return mock_data["lens-manufacturer"]
    
    def get_exif_lens_model(self):
        if self.imageExif:
            return self.imageExif.get("lens-model",mock_data["lens-model"])
        return mock_data["lens-model"]
    
    def get_exif_exposure_time(self):
        if self.imageExif:
            return self.imageExif.get("exposure-time",mock_data["exposure-time"])
        return mock_data["exposure-time"]
    
    def get_exif_iso(self):
        if self.imageExif:
            return self.imageExif.get("iso",mock_data["iso"])
        return mock_data["iso"]

    def get_exif_focal_length(self):
        if self.imageExif:
            return self.imageExif.get("focal-length",mock_data["focal-length"])
        return mock_data["focal-length"]
    
    def get_exif_camera_manufacturer(self):
        if self.imageExif:
            return self.imageExif.get("camera-manufacturer",mock_data["camera-manufacturer"])
        return mock_data["camera-manufacturer"]
      
    def get_exif_camera_model(self):
        if self.imageExif:
            return self.imageExif.get("camera-model",mock_data["camera-model"])
        return mock_data["camera-model"]

    def get_exif_fstop(self):
        if self.imageExif:
            return self.imageExif.get("fstop",mock_data["fstop"])
        return mock_data["fstop"]

    def get_exif_flash(self):
        if self.imageExif:
            return self.imageExif.get("flash",mock_data["flash"])
        return mock_data["flash"]

    def get_exif_gps_longitude(self):
        if self.imageExif:
            return self.imageExif.get("gps-longitude",mock_data["gps-longitude"])
        return mock_data["gps-longitude"]
    
    def get_exif_gps_latitude(self):
        if self.imageExif:
            return self.imageExif.get("gps-latitude",mock_data["gps-latitude"])
        return mock_data["gps-latitude"]
    
    def get_exif_gps_altitude(self):
        if self.imageExif:
            return self.imageExif.get("gps-altitude",mock_data["gps-altitude"])
        return mock_data["gps-altitude"]
    
    def get_exit_xresolution(self):
        if self.imageExif:
            return self.imageExif.get("x-resolution",mock_data["x-resolution"])
        return mock_data["x-resolution"]

    def get_exit_yresolution(self):
        if self.imageExif:
            return self.imageExif.get("y-resolution",mock_data["y-resolution"])
        return mock_data["y-resolution"]
    
    def __repr__(self):
        return "Image: ID {} - url {} - fstop {}".format(self.get_id_image(), self.get_image_url(), self.get_exif_fstop())



