object `Basic Calculator III` {
    import scala.collection.mutable.ArrayBuffer

    object Solution {
        def calculate(s: String): Int = {
            var expr = s.filter(_!=' ').replace("(-", "(0-")
            if(expr.startsWith("-")) {
                expr = "0" + expr
            }
            val post = in2post(expr)
            // println(post.toList)
            evalRPN(post).toInt
        }

        def evalRPN(tokens: Array[String]): Long = {
            var st = List[Long]()
            val ops = Map[String, (Long, Long) => Long](
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
                        st = token.toLong::st
                    }
                }
            }
            st.head
        }

        def isPriorTo(a: Char, b: Char): Boolean = (a=='*'||a=='/') && (b=='+'||b=='-')

        def in2post(expr: String): Array[String] = {
            var opStack = List[Char]()
            val ret = ArrayBuffer[String]()
            var i = 0
            while(i < expr.size) {
                //println(expr(i))
                expr(i) match {
                    case '(' => {
                        opStack = '('::opStack
                        i += 1
                    }
                    case ')' => {
                        while(opStack.head != '(') {
                            ret.append(opStack.head.toString)
                            opStack = opStack.tail
                        }
                        opStack = opStack.tail
                        i += 1
                    }
                    case '+' | '-' | '*' | '/' => {
                        while(!opStack.isEmpty && opStack.head!='(' && !isPriorTo(expr(i), opStack.head)) {
                            ret.append(opStack.head.toString)
                            opStack = opStack.tail
                        }
                        opStack = expr(i)::opStack
                        i += 1
                    }
                    case _ => {
                        var k = i
                        while(k<expr.size && expr(k)>='0' && expr(k)<='9')
                            k += 1
                        ret.append(expr.substring(i, k))
                        i = k
                    }
                }
            }
            while(!opStack.isEmpty) {
                ret.append(opStack.head.toString)
                opStack = opStack.tail
            }
            ret.toArray
        }
    }
}
