"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def __init__(self):
        self.buf_index=0
        self.buf=['']*4
        self.buf_size=0
    
    # abcdefg
    # ab    self.buf_size=4    
    # abcd self.buf
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf_index=0
        while buf_index<n:
            while buf_index<n and self.buf_index<self.buf_size:
                buf[buf_index]=self.buf[self.buf_index]
                buf_index+=1
                self.buf_index+=1
        
            if self.buf_index==self.buf_size:
                self.buf_index=0
                self.buf_size=read4(self.buf)
        
            if self.buf_size==0:
                break
        
        return buf_index
        