class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def sumCalculator(root: TreeNode, is_left_child: bool, is_not_root_node: bool):
            if root == None:
                return 0
            
            if root.right == None and root.left == None:
                if is_not_root_node and is_left_child:
                    #print(root.val) prints the values of individual left leaf nodes
                    return root.val
                else:
                    return 0
            
            total = 0
            total += sumCalculator(root.right, False, True) + sumCalculator(root.left, True, True)
            
            return total
                
        return sumCalculator(root, False, False)

# Driver Code 
if __name__ == "__main__":
  root = TreeNode(3)
  root.left = TreeNode(9)
  root.left.right = TreeNode(12)
  sol = Solution()
  print(sol.sumOfLeftLeaves(root))
