class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP and self.checkIPv4(IP):
            return "IPv4"
        elif ':' in IP and self.checkIPv6(IP):
            return "IPv6"
        else:
            return "Neither"
    
    
    def checkIPv4(self, IP):
        numbers = IP.split('.')
        if len(numbers) != 4: return False
        for num in numbers:
            for n in num:
                if n not in '0123456789':
                    return False            
            if not num or (num[0] == '0' and len(num) > 1) or int(num) > 255:
                return False
        return True
    
    
    def checkIPv6(self, IP):
        if "::" in IP: return False
        numbers = IP.split(':')
        if len(numbers) != 8: return False
        for num in numbers:
            if len(num) > 4: return False
            for n in num:
                if n not in '0123456789abcdefABCDEF':
                    return False
        return True           