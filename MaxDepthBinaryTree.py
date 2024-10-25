# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, depth):
        
        # you find a leaf
        if node.left == None and node.right == None:
            return depth
        
        # what if this node is not a leaf
        # three situations:
        # left child only
        if node.right == None:
            return self.dfs(node.left, depth+1)
        elif node.left == None:
            return self.dfs(node.right, depth+1)
        else:
            return max( self.dfs(node.left, depth+1), self.dfs(node.right, depth+1) )
        
    # Problem 104
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # maximum depth:  the number of nodes along the longest path 
        # from the root node down to the farthest leaf node.

        if root == None: 
            return 0
        else:
            return self.dfs(root, 1)


        