class ListNode:
    """   def __init__(self, value):
           self.val = value
           print(self.val)

       @classmethod
       def from_iter(cls, iterk):
           try:
               temp = next(iterk)
               cls.val = temp

               # print(iterk.index())
               print(cls.val)
               cls.next = ListNode.from_iter(iterk)
           except:
               pass"""


def insert_new_node(head, value):
    temp = ListNode(value)
    temp.next = head.next
    head.next = temp
    return head


def create_many_nodes(list_values: list) -> ListNode:
        head = ListNode()

        while len (list) != 0:
            head.val= list[0]
            head
        return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    nodelist1 = create_many_nodes(list)
    print(nodelist1)
