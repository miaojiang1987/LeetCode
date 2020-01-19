object `Maximum Size Subarray Sum Equals k` {
    import scala.collection.mutable.{Map, HashMap}

    object Solution {
        def maxSubArrayLen(nums: Array[Int], k: Int): Int = {
            val sumMap = HashMap[Int, Int]()
            sumMap.put(0, -1)
            var sum = 0
            var ret = 0
            for(i <- 0 until nums.size) {
                sum += nums(i)
                if(sumMap.contains(sum - k)) {
                    val j = sumMap(sum - k)
                    //println("sum=", sum, j, i)
                    ret = math.max(ret, i - j)
                }
                if(!sumMap.contains(sum))
                    sumMap.put(sum, i)
            }
            //println(sumMap)
            ret
        }
    }
}
