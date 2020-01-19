object `Evaluate Reverse Polish Notation` {
    object Solution {
        def evalRPN(tokens: Array[String]): Int = {
            var st = List[Int]()
            val ops = Map[String, (Int, Int) => Int](
                "+" -> {_+_},
                "-" -> {_-_},
                "*" -> {_*_},
                "/" -> {_/_})

            for(token <- tokens) {
                token match {
                    case "+" | "-" | "*" | "/" => {
                        val b = st.head
                        st = st.tail
                        val a = st.head
                        st = st.tail
                        st = ops(token)(a, b)::st
                    }
                    case _ => {
                        st = token.toInt::st
                    }
                }
            }
            st.head
        }
    }
}
