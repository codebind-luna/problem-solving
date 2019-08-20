# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if (root is None):
            return "" 
    
        q = [root]
        ans = ""
        while q:
            curr = q.pop(0)
            if (curr is None):
                ans += " null"
            else:
                ans += " "+str(curr.val)
                if (curr.left is not None):
                    q.append(curr.left)
                else:
                    q.append(None)
                if (curr.right is not None):
                    q.append(curr.right)
                else:
                    q.append(None)    
        return str(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
      
    
        if (len(data) == 0):
            return None
    
        vals = data.split(' ')[1:]

        root = TreeNode(vals[0])
        q = [root]
        for i in range(1,len(vals),2):
            parent = q.pop(0)
            if (vals[i] != "null"):
                a = TreeNode(vals[i])
                parent.left = a
                q.append(a)
            else:
                parent.left = None

            if (vals[i+1] != "null"): 
                b = TreeNode(vals[i+1])
                parent.right = b
                q.append(b)
            else:
                parent.right = None
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))