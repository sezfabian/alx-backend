#!/usr/bin/python3
"""LRU Caching module
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching System
    """
    # Track keys accessed by get
    accessed_keys = deque()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.update({key: item})
            if key in self.accessed_keys:
                self.accessed_keys.remove(key)
            self.accessed_keys.append(key)
            return

        if len(self.cache_data) == self.MAX_ITEMS:
            if key in self.accessed_keys:
                self.accessed_keys.remove(key)
            lru_key = self.accessed_keys.popleft()
            print("DISCARD: {}".format(lru_key))
            self.cache_data.pop(lru_key)

        self.cache_data[key] = item
        self.accessed_keys.append(key)

    def get(self, key):
        """Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None

        if key in self.accessed_keys:
            self.accessed_keys.remove(key)

        self.accessed_keys.append(key)

        return self.cache_data.get(key)
