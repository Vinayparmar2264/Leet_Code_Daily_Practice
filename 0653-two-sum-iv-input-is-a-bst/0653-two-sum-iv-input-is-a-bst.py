# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        result = []
        inorder(root)

        i = 0
        j = len(result)-1

        while i<j:
            if result[i] + result[j] == k:
                return True
            elif result[i] + result[j] > k:
                j -= 1
            else:
                i += 1
        return False