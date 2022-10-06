"""
File:          sort.py
File Created:  2022-10-05 23:50:31
Author:        callmexss (callmexss@126.com)
Description:   handy sort tools.
"""

import time


class SortHandy:
    def is_sorted(self, arr):
        """Check whether an array is sorted.
        
        Arguments:
            arr (list) -- an array
        
        Returns:
            bool -- True if array is sorted else False
        """
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def test_sort(self, sort_func, arr):
        start = time.perf_counter()
        sort_func(arr)
        end = time.perf_counter()
        assert self.is_sorted(arr)

        print(f"{sort_func.__name__} : {(end - start)} s")


if __name__ == "__main__":
    sh = SortHandy()
    sh.test_sort(sorted, range(int(1e6)))
