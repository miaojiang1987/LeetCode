class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dic = {}
        cnt = 0
        for c in order:
            dic[c] = cnt
            cnt += 1

        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            
            length = min(len(w1), len(w2))
            for j in range(length):
                if w1[j] != w2[j]:
                    if dic[w1[j]] > dic[w2[j]]:
                        return False
                    elif dic[w1[j]] < dic[w2[j]]:
                        break
                        
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            
        return True
            