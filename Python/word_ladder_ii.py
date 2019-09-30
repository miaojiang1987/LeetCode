class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if not wordList:
            return []
        if endWord not in wordList:
            return []
        

        wordList = set(wordList)
        res = []
        dis = {}  #record the distance between start to node's parent
        dq = collections.deque()
        dq.append((beginWord, [beginWord])) # word, path
        
        level = 1
        while dq:
            level_size = len(dq)
            found = False
            for _ in range(level_size):
                curWord, path = dq.popleft()
                w_list = []
                # Get all match nodes in this level
                for i in range(len(curWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if curWord[i] == c:
                            continue
                        nextWord = curWord[:i]+c+curWord[i+1:]
                        if nextWord in wordList:
                            w_list.append(nextWord)  
                # Go over and check potential nodes 
                for w in w_list:
                    # ***special case has to be handled 
                    # tex  >  tax 
                    # tad  >  tax
                    # tax in the same level could be used twice or more.
                    
                    # if the word appeared in "previous" levels, skip it
                    
                    if w in dis and dis[w] < level: 
                        continue

                    if w == endWord:
                        found = True
                        res.append(path+[w])   
                    else:
                        dis[w] = level
                        dq.append((w, path+[w]))
            
            level += 1       
            if found:
                break