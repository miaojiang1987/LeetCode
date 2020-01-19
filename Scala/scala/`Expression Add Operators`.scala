object `Expression Add Operators` {
    import scala.collection.mutable.{ArrayBuffer, HashMap, Map}
    import scala.util.control.Breaks.{break, breakable}
    import scala.math.BigInt


    object Solution {
        def addOperators(num: String, target: Int): List[String] = {
            val sol = ArrayBuffer[String]()
            addOperators(num, BigInt(target), new StringBuilder(), sol, BigInt(0), BigInt(0), 0)
            sol.toList
        }

        def addOperators(num: String, target: BigInt, cur: StringBuilder, sol: ArrayBuffer[String], value: BigInt, delta: BigInt, start: Int): Unit = {
            if(start >= num.size) {
                if(target == value) {
                    sol.append(cur.toString)
                    return
                }
            }
            val curLen = cur.length
            breakable {
                for (i <- start until num.size) {
                    val next = num.substring(start, i + 1)
                    val nextVal = BigInt(next)
                    if (cur.size > 0) {
                        cur.append('+' + next)
                        addOperators(num, target, cur, sol, value + nextVal, nextVal, i + 1)
                        cur.setLength(curLen)

                        cur.append('-' + next)
                        addOperators(num, target, cur, sol, value - nextVal, -nextVal, i + 1)
                        cur.setLength(curLen)

                        cur.append('*' + next)
                        addOperators(num, target, cur, sol, value - delta + delta*nextVal, delta*nextVal, i + 1)
                        cur.setLength(curLen)
                    }
                    else {
                        cur.append(next)
                        addOperators(num, target, cur, sol, nextVal, nextVal, i + 1)
                        cur.setLength(curLen)
                    }
                    if (num(start) == '0')
                        break
                }
            }
        }
    }
}
