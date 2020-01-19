object `Longest Substring with At Most K Distinct Characters` {
    import scala.collection.mutable.{Map, HashMap}
    import scala.util.control.Breaks.{break, breakable}

    object Solution {
        def lengthOfLongestSubstringKDistinct(s: String, k: Int): Int = {
            if(s.isEmpty || k <= 0)
                return 0
            var p = (0, -1)
            var ret = 0
            val cmap = Map[Char, Int]()
            while(p._2 < s.size - 1) {
                p = expand(s, k, p, cmap)
                //println("expanded", s.substring(p._1, p._2 + 1), cmap)
                ret = math.max(p._2 - p._1 + 1, ret)
                p = reduce(s, k, p, cmap)
                //println("reduced", s.substring(p._1, p._2 + 1), cmap)
            }
            ret
        }

        def expand(s: String, k: Int, p: (Int, Int), cmap: Map[Char, Int]): (Int, Int) = {
            val p0 = p._1; var p1 = p._2
            breakable {
                while(p1 < s.size - 1) {
                    if(cmap contains s(p1 + 1)) {
                        cmap(s(p1 + 1)) += 1
                    }
                    else {
                        if(cmap.size == k)
                            break
                        cmap.put(s(p1 + 1), 1)
                    }
                    p1 += 1
                }
            }
            (p0, p1)
        }

        def reduce(s: String, k: Int, p: (Int, Int), cmap: Map[Char, Int]): (Int, Int) = {
            var p0 = p._1; val p1 = p._2
            breakable {
                while(p0 <= p1) {
                    if(cmap.size < k)
                        break
                    cmap(s(p0)) -= 1
                    if(cmap(s(p0)) == 0)
                        cmap.remove(s(p0))
                    p0 += 1
                }
            }
            (p0, p1)
        }
    }
}
