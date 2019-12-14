class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A)!=len(B):
            return -1
        if not A or not B:
            return -1
        hashmap_a={}
        hashmap_b_not_a={}
        for i in range(len(A)):
            if A[i] not in hashmap_a:
                hashmap_a[A[i]]=1
            else:
                hashmap_a[A[i]]+=1
            if B[i]!=A[i]:
                if B[i] not in hashmap_b_not_a:
                    hashmap_b_not_a[B[i]]=1
                else:
                    hashmap_b_not_a[B[i]]+=1
        hashmap_b={}
        hashmap_a_not_b={}
        for i in range(len(B)):
            if B[i] not in hashmap_b:
                hashmap_b[B[i]]=1
            else:
                hashmap_b[B[i]]+=1
            if A[i]!=B[i]:
                if A[i] not in hashmap_a_not_b:
                    hashmap_a_not_b[A[i]]=1
                else:
                    hashmap_a_not_b[A[i]]+=1
        
        switch_a=0
        for key in hashmap_a:
            if hashmap_a[key]==len(A):
                    return 0
            if key in hashmap_b_not_a:
                if hashmap_a[key]+hashmap_b_not_a[key]==len(A):
                    switch_a=hashmap_b_not_a[key]
        
        switch_b=0
        for key in hashmap_b:
            if hashmap_b[key]==len(A):
                    return 0
            if key in hashmap_a_not_b:
                if hashmap_b[key]+hashmap_a_not_b[key]==len(A):
                    switch_b=hashmap_a_not_b[key]

        if switch_a==0 and switch_b==0:
            return -1
        