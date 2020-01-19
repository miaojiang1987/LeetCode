import `Maximum Gap`.Solution.swap

object `Kth Largest Element in an Array` {
    object Solution {

        def swap(nums: Array[Int], a: Int, b: Int): Unit = {
            val temp = nums(a)
            nums(a) = nums(b)
            nums(b) = temp
        }

        private def partition(nums: Array[Int], start: Int, end: Int): Int = {
            if(start == end - 1) {
                if(nums(start) < nums(end))
                    swap(nums, start, end)
                return start
            }
            val mid = start + (end-start) / 2
            swap(nums, mid, start)
            var l = start + 1
            var r = end
            while(l < r) {
                while(l<r && nums(l)>nums(start))
                    l += 1
                while(l<=r && nums(r)<=nums(start))
                    r -= 1
                if(l < r)
                    swap(nums, l, r)
            }
            swap(nums, r, start)
            r
        }

        def findKthLargest(nums: Array[Int], k: Int): Int = {
            var l = 0; var r = nums.size - 1
            while(true) {
                val q = partition(nums, l, r)
                if(q == k-1)
                    return nums(q)
                else if(q < k-1) {
                    l = q + 1
                }
                else {
                    r = q - 1
                }
            }
            0
        }
    }
}
