object `Longest Absolute File Path` {
    object Solution {
        def lengthLongestPath(input: String): Int = {
            val tokens = input.split("\n")
            var st = List[Int]()
            var ret = 0
            for(token <- tokens) {
                val t = token.dropWhile(_ == '\t')
                val level = token.size - t.size
                while(level <= st.size-1) {
                    st = st.tail
                }
                st = t.size::st
                if(t.contains('.'))
                    ret = math.max(ret, st.sum + st.size - 1)
            }
            ret
        }
    }
}
