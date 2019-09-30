class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        index=0
        result=''
        for i in range(len(address)):
            if address[i]!='.':
                result+=address[i]
            else:
                result+='[.]'
        
        return result