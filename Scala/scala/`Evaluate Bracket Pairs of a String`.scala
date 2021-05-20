import scala.collection.mutable.{ArrayBuffer, StringBuilder, HashMap}
object Solution {
    def evaluate(s: String, knowledge: List[List[String]]): String = {
        val cur = new StringBuilder()
        val chunks = getChunks(s)
        val kmap = HashMap[String, String]()
        for(pair <- knowledge)
            kmap.put(pair.head, pair.tail.head)
        for(chunk <- chunks) {
            if((chunk startsWith "(") && (chunk endsWith ")")) {
                cur.append(
                    kmap.getOrElse(chunk.substring(1, chunk.size-1), "?")
                )
            }
            else
                cur.append(chunk)
        }
        cur.toString
    }
    private def getChunks(s: String): Array[String] = {
        val cur = new StringBuilder()
        val chunks = ArrayBuffer[String]()
        for (ch <- s) {
            if (ch == '(') {
                chunks.addOne(cur.toString)
                cur.clear()
                cur.addOne(ch)
            }
            else if (ch == ')') {
                cur.addOne(ch)
                chunks.addOne(cur.toString)
                cur.clear()
            }
            else
                cur.addOne(ch)
        }
        if (!cur.isEmpty)
            chunks.addOne(cur.toString)
        chunks.toArray
    }
}
