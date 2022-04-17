# coding:utf-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        num = []
        while p != None:
            num.append(p.val)
            p = p.next

        sign = 1
        cnt = 0
        while cnt < len(num):
            tmp = []
            if sign % 2 == 0:
                if cnt + 1 + sign - 1 < len(num):
                    tmp = num[cnt:cnt + sign]
                    tmp.reverse()
                else:
                    tmp = num[cnt:len(num)]
                    if (len(num) - cnt) % 2 == 0:
                        tmp.reverse()
            else:
                if cnt + sign > len(num) and (len(num) - cnt) % 2 == 0:
                    tmp = num[cnt:len(num)]
                    tmp.reverse()

            for i in range(len(tmp)):
                num[cnt + i] = tmp[i]

            cnt += sign
            sign += 1

        p = head
        for n in num:
            p.val = n
            p = p.next

        return head


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
