# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        count = 0
        curr = head
        critical = []
        prev = None

        while curr and curr.next:
            if prev and  prev.val<curr.val>curr.next.val:
                critical.append(count)
            if prev and  prev.val>curr.val<curr.next.val:
                critical.append(count)

            prev = curr
            curr = curr.next
            count += 1

        result = [-1,-1]
        if len(critical)>1:
            min_dis = result[1] = critical[-1] - critical[0]  

            for i in range(len(critical)-1):
                if critical[i+1] - critical[i] < min_dis:
                    min_dis = critical[i+1] - critical[i]
            result[0] =  min_dis
        return result