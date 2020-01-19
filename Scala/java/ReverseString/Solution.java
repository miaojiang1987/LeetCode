package ReverseString;

class Solution {
    public void reverseString(char[] s) {
        for(int i=0; i<s.length/2; i++)
            reverse(s, i, s.length-1-i);
    }

    private void reverse(char[] s, int a, int b) {
        char temp = s[a];
        s[a] = s[b];
        s[b] = temp;
    }
}

