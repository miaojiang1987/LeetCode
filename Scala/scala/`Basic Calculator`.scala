
object `Basic Calculator` {
    import scala.collection.mutable.ArrayBuffer

    object Solution {
        def calculate(s: String): Int = {
            val expr = s.filter(_!=' ')
            val post = in2post(expr)
            println(post.toList)
            evalRPN(post)
        }

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
                        if(!opStack.isEmpty && opStack.head!='(') {
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
