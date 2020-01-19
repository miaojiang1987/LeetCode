object `Wiggle Sort` {
    object Solution {
        def wiggleSort(nums: Array[Int]): Unit = {
            val swap = (a: Array[Int], x: Int, y: Int) => {
                val temp = a(x)
                a(x) = a(y)
                a(y) = temp
            }

            case class Cmptor() {
                var gt = true
                def apply(a: Int, b: Int): Boolean = {
                    //println(gt)
                    val ret = if(gt) a > b else a < b
                    gt = !gt
                    ret
                }
            }
            val cmpt = new Cmptor()
            for(i <- 0 until nums.size - 1) {

                if(cmpt(nums(i), nums(i + 1)))
                    swap(nums, i, i + 1)
            }
        }
    }
}
