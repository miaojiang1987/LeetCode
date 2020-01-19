package EncodeAndDecodeStrings;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str: strs) {
            sb.append('[');
            sb.append(escape(str));
            sb.append(']');
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        int p0 = 0, p1 = 1;
        List<String> ret = new ArrayList<>();
        while(p0 < s.length()) {
            while(!(s.charAt(p1) == ']' && (p1==s.length()-1 || s.charAt(p1+1) == '[')))
                p1++;
            ret.add(unescape(s.substring(p0 + 1, p1)));
            p0 = p1 + 1;
            p1 = p0 + 1;
        }
        return ret;
    }

    private String escape(String s) {
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(c == '[' || c == ']')
                sb.append("\\" + c);
            else if(c == '\\')
                sb.append("\\\\");
            else
                sb.append(c);
        }
        return sb.toString();
    }

    private String unescape(String s) {
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(c == '\\') {
                if(i<s.length()-1 && (s.charAt(i+1)=='\\' || s.charAt(i+1)=='[' || s.charAt(i+1)==']')) {
                    sb.append(s.charAt(i + 1));
                    i++;
                }
                else
                    sb.append(c);
            }
            else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

}
