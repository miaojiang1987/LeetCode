class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.freq = 0
        self.content = ""
    
    def __lt__(self,other):
        if self.freq<other.freq:
            return True
        elif self.freq>other.freq:
            return False
        else:
            return self.content>other.content

        
class AutocompleteSystem(object):
    
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.m = collections.defaultdict(int)
        for ind,s in enumerate(sentences):
            self._build(s,times[ind])
        self.acc = ""

        
    def _build(self,sentence,time):
        node = self.root
        for l in sentence:
            if l not in node.child:
                node.child[l] = TrieNode()
            node = node.child[l]
        node.end = True
        node.content = sentence
        self.m[sentence] += time
        node.freq = self.m[sentence]
    
    def _dfs(self,node,h=[]):
        # print(node.content,"content")
        if not node.child or node.end:
            heapq.heappush(h,node)
            if len(h)>3:
                heapq.heappop(h)
        for w in node.child:
            self._dfs(node.child[w],h)
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c=="#":
            self._build(self.acc,1)
            self.acc = ""
            return []
        self.acc += c
        h = []
        node = self.root
        for l in self.acc:
            if l not in node.child:
                return []
            else:
                node = node.child[l]
        self._dfs(node,h)
        ans = []
        while h:
            ans.append(heapq.heappop(h).content)
        return ans[::-1]