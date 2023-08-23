#!/usr/bin/python3
"""LFU Caching module
"""
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush, heapify
from base_caching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching System
    """
    def __init__(self):
        """Initiliaze LFU class
        """
        super().__init__()
        self.frequency = defaultdict(int)  # To keep track of item frequencies
        self.min_heap = []  # Heap to track (frequency, key) pairs

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cleanup(key)  # Remove items if the cache is full

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.update_heap(key)
        else:
            self.cache_data[key] = item
            self.frequency[key] = 1
            heappush(self.min_heap, (1, key))

    def get(self, key):
        """Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.update_heap(key)
        return self.cache_data[key]

    def cleanup(self, key):
        """Remove items if the cache is full
        """
        while len(self.cache_data) >= self.MAX_ITEMS:
            while self.min_heap:
                freq, min_key = heappop(self.min_heap)
                if min_key in self.cache_data and \
                        self.frequency[min_key] == freq:
                    self.cache_data.pop(min_key)
                    self.frequency.pop(min_key)
                    if min_key != key:
                        print("DISCARD: {}".format(min_key))
                    break

            # Rebuild the heap to reflect frequency changes
            temp_heap = []
            for k, freq in self.frequency.items():
                heappush(temp_heap, (freq, k))
            self.min_heap = temp_heap

    def update_heap(self, key):
        """Update the heap to reflect frequency changes
        """
        new_freq = self.frequency[key]
        for i, (freq, k) in enumerate(self.min_heap):
            if k == key:
                self.min_heap[i] = (new_freq, k)
                break
            else:
                heappush(self.min_heap, (new_freq, key))

        # Rebuild the heap to reflect frequency changes
        temp_heap = []
        for k, freq in self.frequency.items():
            heappush(temp_heap, (freq, k))
        self.min_heap = temp_heap
