class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        words = S.split(' ')
        for i in range(len(words)):
            word = words[i]
            if word[0] in 'AaEeIiOoUu':
                res += word+'ma'
            else:
                res += word[1:]+word[0]+'ma'
            res += 'a'*(i+1)
            if i < len(words)-1:
                res += ' '
            
        return res