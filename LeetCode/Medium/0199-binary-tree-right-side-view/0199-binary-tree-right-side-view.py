# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = deque([root])
        output = []

        if root is None:
            return []

        while dq:
            cnt = len(dq)
            for i in range(cnt): 
                root_node = dq.popleft()
                if i == cnt - 1: 
                    output.append(root_node.val) 
                
                if root_node.left:
                    dq.append(root_node.left)
                if root_node.right:
                    dq.append(root_node.right)


        return output