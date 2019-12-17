object `Single Element in a Sorted Array` {
    object Solution {
        def singleNonDuplicate(nums: Array[Int]): Int = {
            //00110011
            //001110011
            //001100011
            assert(nums.size > 0 && nums.size % 2 == 1)
            var start = 0; var end = nums.size - 1
            while(start <= end) {
                //println(start, end)
                if(end == start)
                    return nums(end)
                val mid = start + (end-start)/2
                if(mid%2 == 0) {
                    if(nums(mid) == nums(mid+1)) {
                        start = mid + 2
                    }
                    else {
                        end = mid
                    }
                }
                else {
                    if(nums(mid) == nums(mid-1)) {
                        start = mid + 1
                    }
                    else {
                        end = mid
                    }
                }
            }
            0
        }
    }

}
