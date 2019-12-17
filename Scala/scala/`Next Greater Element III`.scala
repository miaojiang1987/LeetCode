object `Next Greater Element III` {
    import scala.collection.mutable.ArrayBuffer
    import scala.util.control.Breaks.{break, breakable}

    object Solution {
        def nextGreaterElement(n: Int): Int = {
            var buffer = ArrayBuffer[Int]()
            var num = n
            while(num > 0) {
                buffer.append(num % 10)
                num /= 10
            }
            val arr = buffer.toArray.reverse
            if(!nextPermutation(arr))
                return -1
            var ret = 0
            for(d <- arr) {
                if(ret * 10 / 10 != ret)
                    return -1
                ret *= 10
                ret += d
            }
            return ret
        }

        def nextPermutation(nums: Array[Int]): Boolean = {
            if(nums.isEmpty)
                return false
            var i = nums.size - 2
            var glitch = -1
            breakable {
                while( i >= 0 ) {
                    if(nums(i) < nums(i + 1))
                        break
                    i -= 1
                }
            }
            if(i < 0) {
                nums.reverse.copyToArray(nums)
                return false
            }

            glitch = i
            var min = glitch + 1
            for(i <- glitch + 1 until nums.size) {
                if(nums(i) < nums(min) && nums(i) > nums(glitch))
                    min = i
            }
            def swap(nums: Array[Int], start: Int, end: Int): Unit = {
                val temp = nums(start)
                nums(start) = nums(end)
                nums(end) = temp
            }
            swap(nums, glitch, min)
            val last = nums.slice(glitch + 1, nums.size).sorted
            for(i <- glitch+1 until nums.size) {
                nums(i) = last(i- glitch -1)
            }
            return true
        }
    }


}
