# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def dfs(self, node, depth):
    
        if node.left != None or node.right != None:
            if node.left == None:
                return self.dfs(node.right, depth+1)
            elif node.right == None:
                return self.dfs(node.left, depth+1)
            else:
                return min(self.dfs(node.right, depth+1), self.dfs(node.left, depth+1))

        return depth

    
    # Problem 111
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # leaf node: both left and right node are None
        # when you meet a leaf node, return the current depth recorded 
        # back to the parent node and pass the depth back  

        # print(root.left)
        # node = root
        # node.left = None
        # print("node", node)
        # print("root", root)

        if root == None:
            return 0

        min_depth = self.dfs(root, 1)

        return min_depth




        