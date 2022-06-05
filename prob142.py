# coding:utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # 有环直接跳出让随便一个只想头节点以相同的速度再次相遇就是环开始的点
                break

        # 少了一个第二个判断
        if fast is None or fast.next is None:
            return None

        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return slow
