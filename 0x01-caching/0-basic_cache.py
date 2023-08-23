#!/usr/bin/python3
"""BasicCaching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from BaseCaching and is a caching system:
    """
    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
