# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev = head
        curr = head.next
        index = 1

        first_cp = -1
        prev_cp = -1

        min_distance = float("inf")
        max_distance = -1

        while curr.next:

            # Check if current node is a critical point
            if (prev.val < curr.val > curr.next.val) or \
               (prev.val > curr.val < curr.next.val):

                # First critical point
                if first_cp == -1:
                    first_cp = index
                    prev_cp = index

                else:
                    # Update minimum distance
                    min_distance = min(min_distance, index - prev_cp)

                    # Update maximum distance
                    max_distance = index - first_cp

                    # Update previous critical point
                    prev_cp = index

            prev = curr
            curr = curr.next
            index += 1

        if max_distance == -1:
            return [-1, -1]

        return [min_distance, max_distance]