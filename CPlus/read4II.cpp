int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        for (int i=0;i<n;++i){
            if(read_pos==write_pos){
                write_pos=read4(buff);
                read_pos=0;
                if(write_pos==0) return i;
            }
            
            buf[i]=buff[read_pos++];
        }
        return n;
    }
private:
    int read_pos=0,write_pos=0;
    char buff[4];
};