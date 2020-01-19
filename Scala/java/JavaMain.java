import EncodeAndDecodeStrings.Solution;

import java.util.ArrayList;
import java.util.List;

public class JavaMain {
    public static void main(String[] args) {
        Solution sol = new Solution();
        ArrayList<String> list = new ArrayList<>();
        list.add("eeE"); list.add("[");
        String encoded = sol.encode(list);
        System.out.println("encoded=" + encoded);
        List<String> decoded = sol.decode(encoded);
        System.out.println("decoded=" + decoded);
    }
}
