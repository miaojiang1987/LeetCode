object `Minimum Moves to Equal Array Elements` {
    object Solution {
        def minMoves(nums: Array[Int]): Int = {
            val low = nums.min
            nums.map(_ - low).sum
        }
    }
}
