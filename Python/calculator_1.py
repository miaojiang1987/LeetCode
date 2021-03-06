# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:37:05 2019

@author: Owner
"""

'''
计算器
第一題是給你一個string例如"2+3-999"回傳計算結果int，只有加减和数字； 
时间复杂度：O(n), 空间复杂度：O(1)
第二題加上parenthesis 例如"2+((8+2)+(3-999))"一樣回傳計算結果
第三道题加入变量和最简形式。给一个String和一个Map。会给你一个map比如{'a':1, 'b':2, 'c':3}，
假设输入为"a+b+c+1"输出要是7，如果有未定义的变量，比如"a+b+c+1+d"输出就是7+d
'''

def calculator(s):
    result=0
    sign=1
    i=0
    
    while i<len(s):
        if s[i] not in '+-':
            num=''
            while i<len(s) and s[i] not in '+-':
                num+=s[i]
                i+=1
            result+=sign*int(num)
            i-=1
            
        elif s[i]=='+':
            sign=1
        
        elif s[i]=='-':
            sign=-1
        i+=1
    
    return result

print (calculator("2+4-1000+5-10+1000"))
    
        
        