package com.rockthejvm.playground

object `Finding Pairs With a Certain Sum` {
    import scala.collection.mutable.HashMap
    class FindSumPairs(_nums1: Array[Int], _nums2: Array[Int]) {
        val nums1 = _nums1
        val nums2 = _nums2
        val sumMap = HashMap[Int, Int]()
        for(n2 <- nums2) {
            sumMap.put(n2, sumMap.getOrElse(n2, 0) + 1)
        }
        def add(index: Int, `val`: Int) = {
            sumMap(this.nums2(index)) -= 1
            this.nums2(index) += `val`
            sumMap.put(this.nums2(index), sumMap.getOrElse(this.nums2(index), 0) + 1)
        }

        def count(tot: Int): Int = {
            val counts = for{n1 <- this.nums1}
                yield sumMap.getOrElse(tot - n1, 0)
            counts.sum
        }

    }
}
