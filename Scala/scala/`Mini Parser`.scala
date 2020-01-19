object `Mini Parser` {
    /**
     * // This is the interface that allows for creating nested lists.
     * // You should not implement it, or speculate about its implementation
     * class NestedInteger {
     *
     *   // Return true if this NestedInteger holds a single integer, rather than a nested list.
     *   def isInteger: Boolean = {}
     *
     *   // Return the single integer that this NestedInteger holds, if it holds a single integer
     *   def getInteger: Int = {}
     *
     *   // Set this NestedInteger to hold a single integer.
     *   def setInteger(i: Int) = {}
     *
     *   // Return the nested list that this NestedInteger holds, if it holds a nested list
     *   def getList = {}
     *
     *   // Set this NestedInteger to hold a nested list and adds a nested integer to it.
     *   def add(ni: NestedInteger) = {}
     * }
     */
    object Solution {
        def deserialize(s: String): NestedInteger = {
            val isNumber = (ch: Char) => (ch<='9' && ch>='0') || ch=='-'

            if(isNumber(s(0))) {
                val ret = new NestedInteger()
                ret.setInteger(s.toInt)
                return ret
            }
            var i = 0
            var cur: NestedInteger = null
            var st = List[NestedInteger]()

            while(i < s.size) {
                if(s(i) == '[') {
                    if(cur != null)
                        st = cur::st
                    cur = new NestedInteger()
                    i += 1
                }
                else if(isNumber(s(i))) {
                    var end = i+1
                    while(s(end) <= '9' && s(end) >= '0')
                        end += 1
                    val toAdd = new NestedInteger()
                    toAdd.setInteger(s.substring(i, end).toInt)
                    cur.add(toAdd)
                    i = end
                }
                else if(s(i) == ']') {
                    //println(st.size)
                    if(!st.isEmpty) {
                        st.head.add(cur)
                        cur = st.head
                        st = st.tail
                    }
                    i += 1
                }
                else
                    i += 1
            }
            cur
        }
    }

}
