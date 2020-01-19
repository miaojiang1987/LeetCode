object `Majority Element` {
    object Solution {
        def majorityElement(nums: Array[Int]): Int = {
            var c = 0
            var n = 0
            for(d <- nums) {
                if(c == 0) {
                    c = 1
                    n = d
                }
                else {
                    if(d == n)
                        c += 1
                    else {
                        c -= 1
                    }
                }
            }
            n
        }
    }
}
