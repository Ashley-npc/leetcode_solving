class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Linked_List(arr):
    head = None
    switch = None

    for digit in arr:
        new_node = ListNode(digit)
        if head is None:
            head = new_node
            switch = new_node
        else:
            switch.next = new_node
            switch = new_node

    return head

class Solution (object) :
    def addTwoNumbers(self, l1, l2):
        current = l1
        print(current is list)
        number1 = 0
        number2 = 0
        multiplier = 1

        while current :
            number1 += current.val * multiplier
            multiplier *= 10
            current = current.next
            
        current = l2
        multiplier = 1

        while current :
            number2 += current.val * multiplier
            multiplier *= 10
            current = current.next
        
        total = number1 + number2
        total = [int(x) for x in str(total)]
        head = None
        switch = None

        return Linked_List(total[::-1])

l1 = Linked_List([2,4,3])
l2 = Linked_List([5,6,4])
node = Solution().addTwoNumbers(l1, l2)

while node:
    print(node.val)
    node = node.next

