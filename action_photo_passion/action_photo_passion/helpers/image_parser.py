"""Serves as a proxy to decode the content of an image coming fron a webservice call."""

from object_parser import ObjectParser

mock_data = {
    "ID-image": 1,
    "title": "Almudena in Madrid",
    "description": "A superb church in the heart of Madrid",
    "gps-altitude": 0.1254,
    "fstop": 16,
    "flash": 1,
    "gps-longitude": 1.1245,
    "gps-latitude": 0.8754,
    "date-photo": "2024-01-01 10:02:09",
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
}


class ImageParser(ObjectParser):
    """Tool to get all the data from an image. exifs and more."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize an instance of ImageParser."""
        super().__init__(*args, **kwargs)

    def get_title_image(self):
        """Get the title of an image.

        Returns:
            str: the title of the image.
        """
        return self.get_title()

    def get_description_image(self):
        """Get the description of an image.

        Returns:
            str: the description of the image.
        """
        return self.get_description()

    def get_id_image(self):
        """Get the id of an image.
    
        Returns:
            int: the id of the image.
        """
        return self.get_id()

    def get_image_url(self):
        """Get the url of an image.

        Returns:
            str: the url of the image.
        """
        if self.exif_data:
            return self.exif_data.get(
                "url-image-source", mock_data["url-image-source"]
            )
        return mock_data["url-image-source"]

    def get_exif_version(self):
        """Get the exif version of an image.

        Returns:
            str: the exif version of the image.
        """
        if self.exif_data:
            return self.exif_data.get(
                "exif-version", mock_data["exif-version"]
            )
        return mock_data["exif-version"]

    def get_exif_date_photo_taken(self):
        """Get the date an image was taken.

        Returns:
            str: the date the image was taken.
        """
        if self.exif_data:
            return self.exif_data.get("date-photo", mock_data["date-photo"])
        return mock_data["date-photo"]

    def get_exif_date_photo_edit(self):
        """Get the date an image was edited.

        Returns:
            str: the date the image was edited.
        """
        if self.exif_data:
            return self.exif_data.get("date-edit", mock_data["date-edit"])
        return mock_data["date-edit"]

    def get_exif_lens_manufacturer(self):
        """Get the manufacturer/brand of the lens.

        Returns:
            str: the manufacturer/brand of the lens.
        """
        if self.exif_data:
            return self.exif_data.get(
                "lens-manufacturer", mock_data["lens-manufacturer"]
            )
        return mock_data["lens-manufacturer"]

    def get_exif_lens_model(self):
        """Get the model or serial number of the lens.

        Returns:
            str: the model or serial number of the lens.
        """
        if self.exif_data:
            return self.exif_data.get("lens-model", mock_data["lens-model"])
        return mock_data["lens-model"]

    def get_exif_exposure_time(self):
        """Get the exposure time for an image.

        Returns:
            str: the exposure time for an image.
        """
        if self.exif_data:
            return self.exif_data.get(
                "exposure-time", mock_data["exposure-time"]
            )
        return mock_data["exposure-time"]

    def get_exif_iso(self):
        """Get the iso value an image was taken.

        Returns:
            str: the iso value an image was taken.
        """
        if self.exif_data:
            return self.exif_data.get("iso", mock_data["iso"])
        return mock_data["iso"]

    def get_exif_focal_length(self):
        """Get the focal length an image was taken.

        Returns:
            str: the focal length an image was taken.
        """
        if self.exif_data:
            return self.exif_data.get(
                "focal-length", mock_data["focal-length"]
            )
        return mock_data["focal-length"]

    def get_exif_camera_manufacturer(self):
        """Get the manufacturer/brand of the camera.

        Returns:
            str: the manufacturer/brand of the camera.
        """
        if self.exif_data:
            return self.exif_data.get(
                "camera-manufacturer", mock_data["camera-manufacturer"]
            )
        return mock_data["camera-manufacturer"]

    def get_exif_camera_model(self):
        """Get the model or serial number of the camera.

        Returns:
            str: the model or serial number of the camera.
        """
        if self.exif_data:
            return self.exif_data.get(
                "camera-model", mock_data["camera-model"]
            )
        return mock_data["camera-model"]

    def get_exif_fstop(self):
        """Get the aperture an image was taken.

        Returns:
            str: the aperture an image was taken.
        """
        if self.exif_data:
            return self.exif_data.get("fstop", mock_data["fstop"])
        return mock_data["fstop"]

    def get_exif_flash(self):
        """Indicate if the flash triggered to tak the shot.

        Returns:
            str: indicate if the flash triggered..
        """
        if self.exif_data:
            return self.exif_data.get("flash", mock_data["flash"])
        return mock_data["flash"]

    def get_exif_gps_longitude(self):
        """Get the longitude gps position.

        Returns:
            str: the longitude gps position.
        """
        if self.exif_data:
            return self.exif_data.get(
                "gps-longitude", mock_data["gps-longitude"]
            )
        return mock_data["gps-longitude"]

    def get_exif_gps_latitude(self):
        """Get the latitude gps position.

        Returns:
            str: the latitude gps position.
        """
        if self.exif_data:
            return self.exif_data.get(
                "gps-latitude", mock_data["gps-latitude"]
            )
        return mock_data["gps-latitude"]

    def get_exif_gps_altitude(self):
        """Get the altitude gps position.

        Returns:
            str: the altitude gps position.
        """
        if self.exif_data:
            return self.exif_data.get(
                "gps-altitude", mock_data["gps-altitude"]
            )
        return mock_data["gps-altitude"]

    def get_exif_xresolution(self):
        """Get the resolution on x axis of an image.

        Returns:
            str: the resolution on x axis of an image.
        """
        if self.exif_data:
            return self.exif_data.get(
                "x-resolution", mock_data["x-resolution"]
            )
        return mock_data["x-resolution"]

    def get_exif_yresolution(self):
        """Get the resolution on y axis of an image.

        Returns:
            str: the resolution on y axis of an image.
        """
        if self.exif_data:
            return self.exif_data.get(
                "y-resolution", mock_data["y-resolution"]
            )
        return mock_data["y-resolution"]

    def __repr__(self):
        """Display the representation of an instance of this object."""
        return "Image: ID {} - url {} - fstop {}".format(
            self.get_id_image(), self.get_image_url(), self.get_exif_fstop()
        )
