class `Majority Element II` {
    object Solution {
        def majorityElement(nums: Array[Int]): List[Int] = {
            var c0 = 0; var c1 = 0
            var n0 = 0; var n1 = 0
            for(d <- nums) {
                if(c0>0 && n0==d) {
                    c0 += 1
                }
                else if(c1>0 && n1==d) {
                    c1 += 1
                }
                else if(c0 == 0) {
                    n0 = d
                    c0 = 1
                }
                else if(c1 == 0) {
                    n1 = d
                    c1 = 1
                }
                else {
                    c1 -= 1
                    c0 -= 1
                }
            }
            var cc0 = 0; var cc1 = 0
            for(d <- nums) {
                if(d==n0 && c0>0)
                    cc0 += 1
                if(d==n1 && c1>0)
                    cc1 += 1
            }
            var ret = List[Int]()
            if(cc0 > nums.size/3)
                ret = n0::ret
            if(cc1 > nums.size/3)
                ret = n1::ret
            return ret
        }
    }
}
