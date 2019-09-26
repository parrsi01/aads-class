#!/usr/bin/env python3
"""Binary Heap implementation"""


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self):
        """Initializer"""
        self._heap = []
        self._size = 0

    def _perc_up(self, cur_idx):
        """Move a node up"""
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],)
            cur_idx = parent_idx
        #raise NotImplementedError

    def _perc_down(self, cur_idx):
        """Move a node down"""
        while (cur_idx * 2) <= self._size:
            mc = self.get_max_child(cur_idx)
            if self._heap[cur_idx] > self._heap[mc]:
                temp = self._heap[cur_idx]
                self._heap[cur_idx] = self._heap[mc]
                self._heap[mc] = temp
            cur_idx = mc
        #raise NotImplementedError

    def insert(self, item):
        """Add a new item. Optional for this exercise"""
        self._heap.append(item) 
        self._perc_up(len(self._heap) - 1 ) 
        pass

    def delete(self):
        """Remove an item from the heap. Optional for this exercise"""
        self._heap[0], self._heap[ -1] = self._heap[-1 ], self._heap[0] 
        result = self._heap.pop() 
        self._perc_down(0) 
        return result 
        pass

    def heapify(self, not_a_heap):
        """Turn a list into a heap"""
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1
        #raise NotImplementedError

    def get_max_child(self, parent_idx):
        """Get the greater child"""
        if parent_idx * 2+2 > self._size:
            return parent_idx * 2+1
        else:
            if self.heap[parent_idx*2+2] > self.heap[parent_idx*2+1]:
                return parent_idx * 2+2    
            else:
                return parent_idx * 2+1
        #raise NotImplementedError

    def __len__(self):
        """Get heap _"""
        return self.__

    def __str__(self):
        """Heap as a string """
        return str(self._heap)
