object `4Sum II` {
    import scala.collection.mutable.Map

    object Solution {
        def fourSumCount(A: Array[Int], B: Array[Int], C: Array[Int], D: Array[Int]): Int = {
            val map = Map[Int, Int]().withDefaultValue(0)
            for(i <- 0 until A.size; j <- 0 until B.size) {
                map(A(i) + B(j)) += 1
            }
            var ret = 0
            for(i <- 0 until C.size; j <- 0 until D.size) {
                ret += map(- C(i) - D(j))
            }
            ret
        }
    }

}
