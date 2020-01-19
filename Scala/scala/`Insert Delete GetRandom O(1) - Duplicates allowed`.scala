object `Insert Delete GetRandom O(1) - Duplicates allowed` {
    import scala.collection.mutable.{ArrayBuffer, HashSet, Map}
    import scala.util.Random

    class RandomizedCollection() {
        /** Initialize your data structure here. */
        val cache = Map[Int, HashSet[Int]]()
        var arr = ArrayBuffer[Int]()
        val swap = (arr: ArrayBuffer[Int], a: Int, b: Int) => {
            val temp = arr(a)
            arr(a) = arr(b)
            arr(b) = temp
        }
        /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
        def insert(`val`: Int): Boolean = {
            var ret = false
            if (!this.cache.contains(`val`)) {
                ret = true
                cache.put(`val`, HashSet[Int]())
            }
            cache(`val`).add(arr.length)
            arr.append(`val`)
            ret
        }

        /** Removes a value from the set. Returns true if the set contained the specified element. */
        def remove(`val`: Int): Boolean = {
            //println("remove", `val`, arr)
            if(this.cache.contains(`val`)) {
                val idx = cache(`val`).last
                //println("idx", idx)
                cache(`val`).remove(idx)
                if(idx != arr.length - 1) {
                    cache(`val`).remove(idx)
                    cache(arr.last).remove(arr.length - 1)
                    cache(arr.last).add(idx)
                    swap(this.arr, idx, this.arr.length - 1)
                    arr.remove(arr.length - 1)
                }
                else {
                    cache(`val`).remove(idx)
                    arr.remove(arr.length - 1)
                }
                if(cache(`val`).isEmpty)
                    cache.remove(`val`)
                true
            }
            else {
                false
            }
        }

        /** Get a random element from the set. */
        def getRandom(): Int = {
            this.arr(Random.nextInt(arr.length))
        }
    }
}
