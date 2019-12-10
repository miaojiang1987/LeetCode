# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:09:32 2019

@author: Owner
"""

def longestCommon(S,T):
    if not S or not T:
        return None
    
    m,n=len(S),len(T)
    
    dp=[[0]*(n+1) for _ in range(m+1)]
    
    results=set()
    longest=0
    
    for i in range(m):
        for j in range(n):
            if S[i]==T[j]:
                c=dp[i][j]+1
                dp[i+1][j+1]=c
                if c>longest:
                    longest=c
                    results=set()
                    results.add(tuple(S[i-c+1:i+1]))
                elif c==longest:
                    results.add(tuple(S[i-c+1:i+1]))
  
    return results

if __name__=="__main__":
    print (longestCommon(["1","2", "3234.html", "xys.html", "7hsaa.html"],
                        ["1","2", "3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]))
 #   print (longestCommon(["1","2", "3234.html", "xys.html", "7hsaa.html"], ["1","2", "3234.html", "xys.html", "7hsaa.html"]))