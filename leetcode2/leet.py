class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution (object) :
    def addTwoNumbers(self, l1, l2):
        current = l1
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
        total = [int(x) for x in total]
        head = None
        switch = None

        for digit in total[::-1]:
            new_node = ListNode(digit)
            if head is None:
                head = new_node
                switch = new_node
            else:
                switch.next = new_node
                switch = new_node 
        return head

        
node = Solution()
print(node.addTwoNumbers([2,4,3], [5,6,4]))