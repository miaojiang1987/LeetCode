object `House Robber` {
    object Solution {
        def rob(nums: Array[Int]): Int = {
            if(nums.isEmpty)
                return 0
            val isRobbed = Array.fill[Int](nums.length)({0})
            val isNotRobbed = Array.fill[Int](nums.length)({0})
            isRobbed(0) = nums(0)
            for(i <- 1 until nums.length) {
                isRobbed(i) = math.max(isRobbed(i-1), isNotRobbed(i-1) + nums(i))
                isNotRobbed(i) = math.max(isRobbed(i-1), isNotRobbed(i-1))
            }
            math.max(isRobbed.last, isNotRobbed.last)
        }
    }
}
