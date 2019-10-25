class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList:
            return 0
        if endWord not in wordList:
            return 0
        wordList=set(wordList)
        
        queue=collections.deque()
        queue.append(beginWord)
        visited={}
        visited[beginWord]=1
        
        while queue:
            word=queue.popleft()
            if word==endWord:
                return visited[word]
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nextWord=word[:i]+c+word[i+1:]
                    if nextWord in wordList:
                        if nextWord not in visited:
                            visited[nextWord]=visited[word]+1
                            queue.append(nextWord)
        
        
        
        return 0