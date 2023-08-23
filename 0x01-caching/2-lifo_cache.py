#!/usr/bin/python3
"""LIFO caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system
    """
    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
            self.cache_data[key] = item

        elif len(self.cache_data) == self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last_key))
            self.cache_data.pop(last_key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
