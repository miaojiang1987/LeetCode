object `3Sum Smaller` {
    object Solution {
        def threeSumSmaller(nums: Array[Int], target: Int): Int = {
            var ret = 0
            nums.sortInPlaceBy {x: Int => x}
            for(i <- 0 until nums.size-2) {
                var start = i + 1
                var end = nums.size - 1
                while(start < end) {
                    val cur = nums(start) + nums(end) + nums(i)
                    //println(s"cur=$cur")
                    if(cur >= target) {
                        end -= 1
                    }
                    else {
                        ret += end - start
                        start += 1
                    }
                }
            }
            ret
        }
    }
}

