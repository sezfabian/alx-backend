#!/usr/bin/python3
"""FIFO caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system
    """
    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item

        elif len(self.cache_data) == self.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(first_key))
            self.cache_data.pop(first_key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
