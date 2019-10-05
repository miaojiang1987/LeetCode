class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs=path.split('/')
        st=[]
        
        for d in dirs:
            if len(d)==0 or d=='.': 
                continue
            if d=='..':
                if len(st)>0:
                    st.pop()
            
            else:
                st.append(d)
        
        
        if len(st)==0:
            return '/'
        
        else:
            return '/'+'/'.join(st)