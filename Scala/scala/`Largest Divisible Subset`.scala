object `Largest Divisible Subset` {
    import scala.util.Sorting
    object Solution {
        def largestDivisibleSubset(nums: Array[Int]): List[Int] = {
            if(nums.isEmpty)
                return List[Int]()
            val ordinality = Array.fill(nums.size){ List[Int]()}
            Sorting.quickSort(nums)
            ordinality(0) = nums(0)::ordinality(0)
            var ret = ordinality(0)
            for(i <- 1 until nums.size) {
                ordinality(i) = nums(i)::ordinality(i)
                var size = 0
                var idx = -1
                for(k <- i-1 to 0 by -1 if nums(i)%nums(k)==0) {
                    if(ordinality(k).length > size) {
                        size = ordinality(k).length
                        idx = k
                    }
                }
                if(idx >= 0)
                    ordinality(i) = ordinality(i) ++ ordinality(idx)
                if(ret.length < ordinality(i).length)
                    ret = ordinality(i)
            }
            ret
        }
    }
}
