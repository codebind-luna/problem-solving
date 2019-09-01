from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        remains = set(wordList)
        begins = [(beginWord, 1)]
        while begins:
            word, count = begins.pop(0)
            if word == endWord and count > 1:
                return count
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    candi = word[0:i]+c+word[i+1:]
                    if candi in remains:
                        begins.append((candi, count+1))
                        remains.remove(candi)
            
        return 0
