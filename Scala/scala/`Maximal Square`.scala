object `Maximal Square` {
    object Solution {
        def maximalSquare(matrix: Array[Array[Char]]): Int = {
            if(matrix.isEmpty || matrix(0).isEmpty)
                return 0
            val sq = Array.fill(matrix.size)(Array.fill(matrix(0).size)({0}))
            var size = if(matrix.exists(_.exists(_ == '1'))) 1 else 0
            for(j <- 0 until matrix.size)
                sq(j)(0) = if(matrix(j)(0) == '1') 1 else 0
            for(i <- 0 until matrix(0).size)
                sq(0)(i) = if(matrix(0)(i) == '1') 1 else 0

            for(j <- 1 until matrix.size;
                i <- 1 until matrix(0).size) {
                if(matrix(j)(i) == '1') {
                    var last = List[Int](sq(j-1)(i), sq(j)(i-1), sq(j-1)(i-1))
                    sq(j)(i) = if(last.isEmpty) 1 else last.min + 1
                    size = math.max(size, sq(j)(i))
                    // println(s"$j $i ${sq(j)(i)}")
                }
            }
            size * size
        }
    }
}
