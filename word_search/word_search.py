class TrieNode:
    def __init__(self):
        self.if_word = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self,word):
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.if_word = True
        
    def searchWord(self,word):
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return curr.if_word
    
    def searchPrefix(self,prefix):
        curr = self.root
        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        R = len(board)
        if R == 0:
            return []
        C = len(board[0])
        
        seen = set()
        res = set()
        
        def dfs(r,c,curr):
            seen.add((r,c))
            if trie.searchWord(curr):
                res.add(curr)
            nxt_points = {(r+1,c),(r-1,c),(r,c+1),(r,c-1)}
            for nxt_r,nxt_c in nxt_points:
                if 0<=nxt_r<R and 0<=nxt_c<C and trie.searchPrefix(curr+board[nxt_r][nxt_c]) and (nxt_r,nxt_c) not in seen:
                    dfs(nxt_r,nxt_c,curr+board[nxt_r][nxt_c])
            seen.remove((r,c))
        
        for r in range(R):
            for c in range(C):
                if trie.searchPrefix(board[r][c]):
                    dfs(r,c,board[r][c])
        
        return list(res)