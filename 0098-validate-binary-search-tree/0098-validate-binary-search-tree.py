# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,limit):
            if not node :
                return True

            if not limit[0] < node.val < limit[1]:
                return False
                
            left_sub = dfs(node.left,[limit[0],node.val])
            if not left_sub:
                return False
            right_sub = dfs(node.right,[node.val,limit[1]])

            return left_sub and right_sub

        return dfs(root,[float("-inf"),float("inf")])