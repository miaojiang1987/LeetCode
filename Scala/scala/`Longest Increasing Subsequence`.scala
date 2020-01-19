object `Longest Increasing Subsequence` {
    import scala.collection.mutable.{ArrayBuffer, HashMap, Map}

    object Solution {
        def lengthOfLIS(nums: Array[Int]): Int = {
            val arr = ArrayBuffer[Int]()
            for(d <- nums) {
                val pos = bsearch(arr, d)
                if(pos >= arr.length)
                    arr.append(d)
                else {
                    arr(pos) = d
                }
            }
            arr.length
        }

        def bsearch(nums: ArrayBuffer[Int], target: Int): Int = {
            if(nums.isEmpty || target > nums.last)
                return nums.length
            var start = 0; var end = nums.length - 1
            while(start <= end) {
                if(start == end)
                    return if(target <= nums(end)) end else end + 1
                if(start == end - 1) {
                    if(target <= nums(start))
                        return start
                    if(target <= nums(end))
                        return end
                    return end + 1
                }
                val mid = start + (end-start) / 2
                if(target <= nums(mid))
                    end = mid
                else
                    start = mid
            }
            -1
        }
    }
}
