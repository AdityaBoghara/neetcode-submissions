# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder or not inorder:  # Moved to top
                return None

            indices = {val: idx for idx, val in enumerate(inorder)}

            root = TreeNode(preorder[0])  # Wrap in TreeNode
            mid = indices[root.val]       # Use root.val to index

            root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
            return root