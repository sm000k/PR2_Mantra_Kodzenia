from functools import singledispatchmethod
from typing import List

import self


class ListNode:
    @singledispatchmethod
    def __init__(self):
        # This is the default implementation. Runs when the data type is not registered.
        raise ValueError("This data type is not supported.")

    def __init__( iterk):

        try:
            temp = next(iterk)
            self.val = temp
            print(self.val)
            print(type(iterk))
            self.next = ListNode(iterk)
        except StopIteration:
            pass

    def __init__(self, value, next=None):
        self.val = value
        print(self.val)
        self.next = next


if __name__ == "__main__":
    # heed = ListNode(iter([1, 2, 3, 4, 5]))
    # hed = ListNode(10)
    x = iter([1, 2, 3, 4, 5])
    isinstance(iter, (x,x))
