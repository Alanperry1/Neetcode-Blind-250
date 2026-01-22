# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time Complexity: O(n) - visit each node once where n is total nodes in both trees
        # Space Complexity: O(h) - recursion stack depth where h is tree height
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        else:
            return False
