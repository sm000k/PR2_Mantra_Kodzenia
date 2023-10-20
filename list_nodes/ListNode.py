from functools import singledispatchmethod
from typing import List, Union, Iterable

import self


class ListNode:
    @singledispatchmethod
    def __init__(self, input_val: Union[Iterable, int]):
        raise ValueError("This data type is not supported.")

    @__init__.register
    def init_iter(self, iterk):

        try:
            temp = next(iterk)
            self.val = temp
            print(self.val)
            print(type(iterk))
            self.next = ListNode(iterk)
        except StopIteration:
            pass

    @__init__.register(int)
    def costam(self, value):
        self.val = value
        print(self.val)


if __name__ == "__main__":
    # heed = ListNode(iter([1, 2, 3, 4, 5]))
    hed = ListNode(10)
    # x = iter([1, 2, 3, 4, 5])
    # isinstance(iter, (x,x))