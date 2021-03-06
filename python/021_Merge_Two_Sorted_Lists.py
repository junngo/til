"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next

            tail = tail.next

        tail.next = l1 or l2

        return head.next

    def mergeTwoLists_recusive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists_recusive(l1.next, l2)
        return l1

if __name__ == "__main__":
    ln1, ln1.next, ln1.next.next = ListNode(1), ListNode(2), ListNode(5)
    ln2, ln2.next, ln2.next.next = ListNode(5), ListNode(6), ListNode(7)

    resultVar = Solution().mergeTwoLists_recusive(ln1, ln2)
    print("{0} -> {1} -> {2} -> {3} -> {4} ->{5}".format(
        resultVar.val,
        resultVar.next.val,
		resultVar.next.next.val,
		resultVar.next.next.next.val,
        resultVar.next.next.next.next.val,
        resultVar.next.next.next.next.next.val))
