object `Range Sum Query - Mutable` {
    class NumArray(_nums: Array[Int]) {
        private val nums = Array.ofDim[Int](_nums.length)
        private val bitree = Array.ofDim[Int](nums.length + 1)
        this.init()

        def init(): Unit = {
            for(i <- 0 until _nums.size) {
                update(i, _nums(i))
                nums(i) = _nums(i)
            }
        }


        def update(i: Int, `val`: Int): Unit = {
            var idx = i + 1
            val delta = `val` - nums(i)
            while(idx <= nums.length) {
                bitree(idx) += delta
                idx += idx & (-idx)
            }
            nums(i) = `val`
            //println(s"updated(${i}, ${`val`} bitree", bitree.toList)
        }

        def sum(i: Int): Int = {
            var idx = i + 1
            var ret = 0
            while(idx >= 1) {
                ret += bitree(idx)
                idx -= idx & (-idx)
            }
            ret
        }

        def sumRange(i: Int, j: Int): Int = {
            if(i > 0)
                sum(j) - sum(i - 1)
            else
                sum(j)
        }
    }
}
