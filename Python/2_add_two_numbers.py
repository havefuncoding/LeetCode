# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.getNumberDigitsReversed(l1)
        n2 = self.getNumberDigitsReversed(l2)
        return self.getHeadNodeOfSumReversed(n1 + n2)
    
    
    def getNumberDigitsReversed(self, l):
        """
        :type l: ListNode, head to tail gets digits reversed
        :rtype: int, return accumulation of digits from tail to head
        """
        current = l         # Get a copy of the head node
        num = 0             # Track digits right to left, using times_place
        times_place = 1     # Track times place, ones, tens, ...
        
        while current:
            num = num + times_place * current.val
            times_place *= 10
            current = current.next
        return num
    
    
    def getHeadNodeOfSumReversed(self, n):
        """
        :type n: int
        :rtype: ListNode, head should contain last digit of n
        """
        head = ListNode(n % 10)
        current = head
        n //= 10
        
        while n > 0:
            current.next = ListNode(n % 10)
            n //= 10
            current = current.next
        
        #self.printDigitsHeadToTail(head)
        return head    
    
    
    def printDigitsHeadToTail(self, l):
        """
        :type l: ListNode, head node of linked list
        :rtype: void, prints digits from head to tail
        """
        current = l
        while current:
            print(current.val, end=" ")
            current = current.next
            
