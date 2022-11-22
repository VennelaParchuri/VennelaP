# LeetCode problem 24 Swap Node Pairs

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        prev = dummy
        cur = head

        while cur and cur.next:
            second = cur.next
            third = cur.next.next

            second.next = cur
            cur.next = third
            prev.next = second

            prev = cur
            cur = third
        return dummy.next