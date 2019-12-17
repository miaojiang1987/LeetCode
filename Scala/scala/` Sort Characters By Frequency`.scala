object ` Sort Characters By Frequency` {
    object Solution {
        def frequencySort(s: String): String = {
            val counter = s.foldLeft(Map[Char, Int]())({
                (map: Map[Char, Int], ch: Char) =>
                    map + (ch -> (map.getOrElse(ch, 0) + 1))
            })
            val counts = counter.toSeq
            //println(counts)
            val sb = new StringBuilder()
            for ((ch, f) <- counts.sortBy(_._2).reverse) {
                for(_ <- 0 until f)
                    sb.append(ch)
            }
            sb.toString
        }
    }

}
