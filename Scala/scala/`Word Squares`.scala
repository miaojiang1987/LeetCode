object `Word Squares` {
    import scala.collection.mutable.ArrayBuffer

    object Solution {

        case class Node(value: Char){
            val next = Array.ofDim[Node](26)
            var words = List[Int]()
            def add(w: Int): Unit = {
                words = w::words
            }
        }

        /** Inserts a word into the trie. */
        def insert(root: Node, word: String, i: Int): Unit = {
            var cur = root
            cur.add(i)
            for(c <- word) {
                val idx: Int = c - 'a'
                if(cur.next(idx) == null)
                    cur.next(idx) = Node(c)
                cur = cur.next(idx)
                cur.add(i)
            }
        }

        def wordSquares(root: Node, words: Array[String], cur: List[Int], sol: ArrayBuffer[List[String]]): Unit = {
            if(cur.size == words.last.size) {
                sol.append(cur.map(words(_)))
                return
            }
            var curNode = root
            val chIndex = cur.size
            for(i <- cur.reverse) {
                val nextCh = words(i).charAt(chIndex)
                //println("nextCh", nextCh)
                val nextId: Int = nextCh - 'a'
                curNode = curNode.next(nextId)
                //println("next curNode", curNode)
                if(curNode == null)
                    return
            }

            for(i <- curNode.words) {
                wordSquares(root, words, i::cur, sol)
            }
        }

        def wordSquares(words: Array[String]): List[List[String]] = {
            val sol = ArrayBuffer[List[String]]()
            val root = Node(0)
            for(i <- 0 until words.size) {
                insert(root, words(i), i)
            }
            wordSquares(root, words, List(), sol)
            sol.toList.map(_.reverse)
        }
    }

}
