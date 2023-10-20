class ListNode:
    def __init__(self, value):
        self.val = value
        print(self.val)

    @classmethod
    def from_iter(cls, iterk):
        try:
            temp = next(iterk)
            cls.val = temp
            print(cls.val)
            cls.next = ListNode.from_iter(iterk)
        except StopIteration:
            pass


if __name__ == "__main__":

    ListNode(10)
    ListNode.from_iter(iter((1, 2, 3, 4, 5)))
