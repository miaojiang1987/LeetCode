object `Bomb Enemy` {
    object Solution {

        def maxKilledEnemies(grid: Array[Array[Char]]): Int = {
            if(grid.isEmpty || grid.last.isEmpty)
                return 0
            val h = grid.size; val w = grid.last.size
            val kills = Array.fill[Array[Int]](h)(Array.ofDim[Int](w))

            for(j <- 0 until h) {
                var visited = List[(Int, Int)]()
                var enemies = 0
                for(i <- 0 until w) {
                    if(grid(j)(i) == 'W') {
                        if(enemies > 0)
                            visited.foreach(
                                {p => kills(p._1)(p._2) += enemies}
                            )
                        enemies = 0
                        visited = List[(Int, Int)]()
                    }
                    else if(grid(j)(i) == 'E') {
                        enemies += 1
                    }
                    else {
                        visited = (j, i)::visited
                    }
                }
                if(enemies > 0)
                    visited.foreach(
                        {p => kills(p._1)(p._2) += enemies}
                    )
            }

            for(i <- 0 until w) {
                var visited = List[(Int, Int)]()
                var enemies = 0
                for(j <- 0 until h) {
                    if(grid(j)(i) == 'W') {
                        if(enemies > 0)
                            visited.foreach(
                                {p => kills(p._1)(p._2) += enemies}
                            )
                        enemies = 0
                        visited = List[(Int, Int)]()
                    }
                    else if(grid(j)(i) == 'E') {
                        enemies += 1
                    }
                    else {
                        visited = (j, i)::visited
                    }
                }
                if(enemies > 0)
                    visited.foreach(
                        {p => kills(p._1)(p._2) += enemies}
                    )
            }
            kills.map(_.max).max
        }
    }
}
