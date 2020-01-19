object `First Unique Character in a String` {
    object Solution {
        def firstUniqChar(s: String): Int = {
            val counter = s.foldLeft(Array.ofDim[Int](26)){
                (cur, ch) =>
                    cur(ch-'a') += 1
                    cur
            }
            val indices = (0 until s.size).filter{(i: Int) => counter(s(i) - 'a') <= 1}
            if(indices.isEmpty) -1 else indices.head
        }
    }
}
