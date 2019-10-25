class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        result=[]
        queue=collections.deque()
        
        if not wordList:
            return None
        
        if endWord not in wordList:
            return None
        hashmap={}
        wordList = set(wordList)
        queue.append((beginWord,[beginWord]))
        found=False
        level=1
        while queue:
            for _ in range(len(queue)):
                word,lst=queue.popleft()
                wlist=[]
                
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if word[i]!=c:
                            nextWord=word[:i]+c+word[i+1:]
                            if nextWord in wordList:
                                wlist.append(nextWord)
                
                for w in wlist:
                    if w in hashmap and hashmap[w] < level: 
                        continue

                    if w == endWord:
                        found = True
                        result.append(lst+[w])   
                    else:
                        hashmap[w] = level
                        queue.append((w, lst+[w]))

            level+=1
            if found==True:
                break
            
        
        
        
        return result