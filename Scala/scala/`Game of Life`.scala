object `Game of Life` {
    object Solution {
        def gameOfLife(board: Array[Array[Int]]): Unit = {
            if(board.size == 0 || board(0).size == 0)
                return
            val next = Array.ofDim[Int](board.size, board(0).size)
            for(j <- 0 until board.size; i<- 0 until board(0).size) {
                val nc = count(board, j, i)
                //println(j, i, nc)
                next(j)(i) = transit(board(j)(i), nc)
            }
            (0 until board.size).foreach{
                (i: Int) => board(i) = next(i)}
        }

        def transit(cur: Int, nc: Int): Int = {
            if(cur == 0) {
                nc match {
                    case 3 => 1
                    case _ => 0
                }
            }
            else {
                nc match {
                    case 2 => 1
                    case 3 => 1
                    case _ => 0
                }
            }
        }

        def count(board: Array[Array[Int]], y: Int, x: Int) = {
            val directions = List((1, 0), (1, 1), (1, -1), (0, 1),
                (0, -1), (-1, 0), (-1, 1), (-1, -1))
            val isBounded = {(y: Int, x: Int) =>
                y>=0 && y<board.length && x>=0 && x<board(0).length}
            var ret = 0
            for((dy, dx) <- directions) {
                if(isBounded(y + dy, x + dx) && board(y + dy)(x + dx)==1)
                    ret += 1
            }
            ret
        }
    }
}
