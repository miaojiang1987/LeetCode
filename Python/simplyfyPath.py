class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs=path.split('/')
        st=[]
        
        for d in dirs:
            if d=='.' or len(d)==0:
                continue
            
            if  d=='..':
                if st:
                    st.pop()
            else:
                st.append(d)
            
        if len(st)==0:
            return "/"
        
        
        return '/'+'/'.join(st)