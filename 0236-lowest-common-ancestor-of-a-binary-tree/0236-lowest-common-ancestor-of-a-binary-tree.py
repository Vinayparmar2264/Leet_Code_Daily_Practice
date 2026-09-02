# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self,node,p,q):
        if node is None:
            return None
        
        if node == p or node == q:
            return node
        
        left = self.solve(node.left,p,q)
        right = self.solve(node.right,p,q)

        if left and right:
            return node

        if left :
            return left
        
        return right


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root,p,q)
     
        