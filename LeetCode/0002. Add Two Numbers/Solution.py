# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        headNode = ListNode()
        prevNode = headNode
        prevRemainder = 0

        while prevRemainder > 0 or l1 or l2:
            currentNode = ListNode()

            if l1:
                prevRemainder += l1.val
                l1 = l1.next

            if l2:
                prevRemainder += l2.val
                l2 = l2.next

            currentNode.val = prevRemainder % 10
            prevRemainder = prevRemainder // 10

            prevNode.next = currentNode
            prevNode = currentNode

        return headNode.next
