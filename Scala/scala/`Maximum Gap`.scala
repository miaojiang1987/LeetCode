object `Maximum Gap` {

    object Solution {
        private def swap(nums: Array[Int], a: Int, b: Int): Unit = {
            val temp = nums(a)
            nums(a) = nums(b)
            nums(b) = temp
        }

        private def partition(nums: Array[Int], start: Int, end: Int): Int = {
            if(start == end - 1) {
                if(nums(start) > nums(end))
                    swap(nums, start, end)
                return start
            }
            val mid = start + (end-start) / 2
            swap(nums, mid, start)
            println(s"pivot=${nums(start)}")
            var l = start + 1
            var r = end
            while(l < r) {
                while(l<r && nums(l)<nums(start))
                    l += 1
                while(l<=r && nums(r)>=nums(start))
                    r -= 1
                if(l < r)
                    swap(nums, l, r)
            }
            swap(nums, r, start)
            println(nums.slice(start, end + 1).toList)
            println(s"l=$l,r=$r")
            r
        }

        private def qsortRec(nums: Array[Int], start: Int, end: Int): Unit = {
            if(start < end) {
                val q = partition(nums, start, end)
                qsortRec(nums, start, q - 1)
                qsortRec(nums, q + 1, end)
            }
        }

        def qsort(nums: Array[Int]): Unit = {
            qsortRec(nums, 0, nums.size - 1)
        }

        def maximumGap(nums: Array[Int]): Int = {
            qsort(nums)
            println(nums.toList)
            val gaps = for {i <- 1 until nums.size}
                yield nums(i) - nums(i-1)
            if(gaps.isEmpty) 0 else gaps.max
        }
    }
}
