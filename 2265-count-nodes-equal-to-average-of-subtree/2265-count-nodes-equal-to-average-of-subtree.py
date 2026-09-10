# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.matching_nodes = 0
        
        def postorder(node):
            if not node:
                # Base case: empty node contributes 0 to sum and 0 to count
                return 0, 0
                
            # 1. Get sum and count from both children
            left_sum, left_count = postorder(node.left)
            right_sum, right_count = postorder(node.right)
            
            # 2. Calculate current node's subtree sum and count
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            # 3. Check the average condition
            if total_sum // total_count == node.val:
                self.matching_nodes += 1
                
            # 4. Pass the calculated values up to the parent
            return total_sum, total_count
            
        postorder(root)
        return self.matching_nodes