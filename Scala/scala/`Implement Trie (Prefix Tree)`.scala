object `Implement Trie (Prefix Tree)` {
    class Trie() {

        /** Initialize your data structure here. */
        case class Node(value: Char){
            val next = Array.ofDim[Node](26)
            var isWord = false
        }
        val root = Node(0)
        /** Inserts a word into the trie. */
        def insert(word: String): Unit = {
            var cur = this.root
            for(c <- word) {
                val idx: Int = c - 'a'
                if(cur.next(idx) == null)
                    cur.next(idx) = Node(c)
                cur = cur.next(idx)
            }
            cur.isWord = true
        }

        /** Returns if the word is in the trie. */
        def search(word: String): Boolean = {
            var cur = this.root
            for(c <- word) {
                val idx: Int = c - 'a'
                if(cur.next(idx) == null)
                    return false
                cur = cur.next(idx)
            }
            cur.isWord == true
        }

        /** Returns if there is any word in the trie that starts with the given prefix. */
        def startsWith(prefix: String): Boolean = {
            var cur = this.root
            for(c <- prefix) {
                val idx: Int = c - 'a'
                if(cur.next(idx) == null)
                    return false
                cur = cur.next(idx)
            }
            true
        }

    }

    /**
     * Your Trie object will be instantiated and called as such:
     * var obj = new Trie()
     * obj.insert(word)
     * var param_2 = obj.search(word)
     * var param_3 = obj.startsWith(prefix)
     */
}
