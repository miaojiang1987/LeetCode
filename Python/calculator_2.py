# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:38:43 2019

@author: Owner
"""

'''
计算器
第一題是給你一個string例如"2+3-999"回傳計算結果int，只有加减和数字； 
第二題加上parenthesis 例如"2+((8+2)+(3-999))"一樣回傳計算結果
第三道题加入变量和最简形式。给一个String和一个Map。会给你一个map比如{'a':1, 'b':2, 'c':3}，
假设输入为"a+b+c+1"输出要是7，如果有未定义的变量，比如"a+b+c+1+d"输出就是7+d
'''

def calculator(s):
    nums=[]
    ops=[]
    i=0
    while i<len(s):
        if s[i] in "0123456789":
            digit=""
            while i<len(s) and s[i] in '0123456789':
                digit+=s[i]
                i+=1
            nums.append(int(digit))
            i-=1
        elif s[i] in '+-':
            ops.append(s[i])
        
        elif s[i]==")":
            op=ops.pop()
            num2=nums.pop()
            num1=nums.pop()
            if op=='-':
                res=num1-num2
            else:
                res=num1+num2
            nums.append(res)
        i+=1

    
    op=ops.pop()
    num2=nums.pop()
    num1=nums.pop()
    
    if op=="+":
        res=num1+num2
    else:
        res=num1-num2
    
    return res

res = calculator("2+((8+2)+(3-999))")
print(res)