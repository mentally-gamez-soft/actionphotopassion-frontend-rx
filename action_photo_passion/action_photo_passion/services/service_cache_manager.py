"""Defines an abstract manager that will handle all the available caches of the application."""

from action_photo_passion.action_photo_passion.helpers.object_parser import (
    ObjectParser,
)


class ServiceCacheManager:
    """Define the super class that will manage all the different available caches of the app."""

    cache: dict = {}

    def add_target_cache_to_cache_inventory(self, cache_key: str):
        """Add a new cache to the existing list of dalready defined caches.

        Args:
            cache_key (str): The symbolic name of the cache to track.
        """
        self.cache[cache_key] = []

    def __retrieve_cache_value__(self, cache_key: str) -> list:
        """Get all the cached elements a specific targeted cache.

        Args:
            cache_key (str): The target cache

        Returns:
            list: All the elements existing in this specific cache.
        """
        return self.cache.get(cache_key)

    def __exists_id_in_cache__(self, cache_key: str, id: int) -> dict:
        """Check the object exist in the specified cache according to an id.

        Args:
            cache_key (str): the targeted cache.
            id (int): the id of the object to search for.

        Returns:
            dict: status (bool) and an instance of objectParser.
        """
        targeted_cache = self.__retrieve_cache_value__(cache_key)

        if targeted_cache:
            element = [obj for obj in targeted_cache if obj.get_id() == id]
            return {"status": len(element) > 0, "obj": element[:]}
        return {"status": False, "obj": None}

    def __exists_obj_in_cache__(
        self, cache_key: str, obj_reader: ObjectParser
    ) -> bool:
        """Check the object exist in the specified cache.

        Args:
            cache_key (str): the targeted cache.
            obj_reader (ObjectParser): an instance of objectParser.

        Returns:
            bool: True if the object exists in cache.
        """
        targeted_cache = self.__retrieve_cache_value__(cache_key)

        if targeted_cache:
            element = [
                obj
                for obj in targeted_cache
                if obj.get_id() == obj_reader.get_id()
            ]
            return len(element) > 0
        return True

    def add_to_cache(self, cache_key: str, obj_reader: ObjectParser):
        """Add an object to the specified cache.

        Args:
            cache_key (str): the cache in which to record the info.
            obj_reader (ObjectParser): the instance of the object.
        """
        if not self.__exists_obj_in_cache__(cache_key, obj_reader):
            self.cache[cache_key].append(obj_reader)

    def get_from_cache(self, cache_key: str, obj_id: int):
        """Return an object in one of the managed cache.

        Args:
            cache_key (str): The target cache to extract the info from.
            obj_id (int): The id of the object to search.

        Returns:
            ObjectParser: An instance of the object.
        """
        res = self.__exists_id_in_cache__(cache_key, obj_id)
        if res["status"]:
            return res["obj"]
