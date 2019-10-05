class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # 先用一个哈希表统计s1中字符的出现次数
        dic = {}
        for c in s1:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
             
        match_count = 0
        l = 0
        for r in range(len(s2)):
            if s2[r] in dic:
                dic[s2[r]] -= 1
                if dic[s2[r]] >= 0:
                    match_count += 1
                    
            while match_count == len(s1):
                if r - l + 1 == len(s1):
                    return True
                
                # decrease window size
                if s2[l] in dic:
                    dic[s2[l]] += 1
                    if dic[s2[l]] > 0:
                        match_count -= 1
                l += 1
                
        return False