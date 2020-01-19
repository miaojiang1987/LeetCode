class `Longest Substring with At Least K Repeating Characters` {
    import scala.collection.immutable.HashMap

    object Solution {
        def longestSubstring(s: String, k: Int): Int = {
            //println("cur string =", s)
            var cur0 = 0; var cur1 = 0
            var ret = 0
            val cmap: HashMap[Char, Int] = s.foldLeft(HashMap[Char, Int]()){
                (cmap: HashMap[Char, Int], ch: Char) =>
                    cmap + (ch -> (cmap.getOrElse(ch, 0) + 1))
            }
            while(cur1 < s.size) {
                if(cmap(s(cur1)) < k) {
                    if(cur0 < cur1) {
                        val sub = s.substring(cur0, cur1)
                        ret = math.max(ret, longestSubstring(sub, k))
                    }
                    cur0 = cur1 + 1
                    cur1 = cur0
                }
                else {
                    cur1 += 1
                }
            }
            if(cur0 == 0 && cur1 == s.size)
                return s.size
            if(cur0 < cur1) {
                val sub = s.substring(cur0, cur1)
                ret = math.max(ret, longestSubstring(sub, k))
            }
            ret
        }
    }
}
