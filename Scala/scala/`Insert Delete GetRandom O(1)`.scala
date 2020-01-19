object `Insert Delete GetRandom O(1)` {
    import scala.collection.mutable.{ArrayBuffer, Map}
    import scala.util.Random

    class RandomizedSet() {
        /** Initialize your data structure here. */
        val cache = Map[Int, Int]()
        var arr = ArrayBuffer[Int]()
        /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
        def insert(`val`: Int): Boolean = {
            if(!this.cache.contains(`val`)) {
                cache.put(`val`, arr.length)
                arr.append(`val`)
                true
            }
            else
                false
        }

        /** Removes a value from the set. Returns true if the set contained the specified element. */
        def remove(`val`: Int): Boolean = {
            if(this.cache.contains(`val`)) {
                val idx = cache(`val`)
                val temp = arr(idx)
                arr(cache(`val`)) = arr.last
                arr(arr.length - 1) = temp

                this.cache.remove(`val`)
                if(idx != arr.length - 1)
                    this.cache(arr(idx)) = idx
                this.arr.remove(arr.length - 1)
                true
            }
            else
                false
        }

        /** Get a random element from the set. */
        def getRandom(): Int = {
            this.arr(Random.nextInt(arr.length))
        }
    }
}
