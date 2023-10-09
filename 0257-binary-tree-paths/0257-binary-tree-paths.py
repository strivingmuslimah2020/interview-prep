# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        
        def dfs(root , path):
            
            if not root:
                return
            if root.left is None and root.right is None:
                path += str(root.val)
                answer.append(path)
                
            dfs(root.left , path + str(root.val) + "->")
            dfs(root.right , path + str(root.val) + "->")
            
        dfs(root , "")
        
        result = []
        
        for path in answer:
            result.append("".join(path))
            
        return result