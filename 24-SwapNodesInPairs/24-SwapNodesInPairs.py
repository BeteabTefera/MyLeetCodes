# Last updated: 8/18/2026, 2:50:50 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        ans = head.next
        cur = head # cur points to head (odd pos)
        prev = None

        while cur:
            if cur.next: # cur is 1, cur.next is 2/
                adj = cur.next # save 2/
                cur.next = cur.next.next # 1 to 3/
                adj.next = cur # 2 to 1/
                if prev: # cur is not head
                    prev.next = adj # 1 to 4
                prev = cur # prev is 1
            cur = cur.next # 1 move to 3/
        return ans