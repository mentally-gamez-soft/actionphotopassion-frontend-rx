from action_photo_passion.services.service_cache_manager import (
    ServiceCacheManager,
)

cache = ServiceCacheManager()


def get_cache_application():
    return cache
