package com.rockthejvm.playground




object `Closest Room` {
    import scala.collection.mutable.TreeSet
    import scala.collection.mutable.ArrayBuffer
    import scala.math.Ordering
    import scala.math.abs

    def closestRoom(rooms: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
        val roomsBySize = rooms.sortBy(_(1)).reverse
        val queriesIndicesByMinSize = queries.zipWithIndex.sortBy(_._1(1)).map(_._2).reverse
        val answers = ArrayBuffer[(Int, Int)]()
        val roomIDSet = new TreeSet[(Int, Int)]()(Ordering.by[(Int, Int), Int](_._1))
        var i = 0
        for(qid <- queriesIndicesByMinSize) {
            val query = queries(qid)
            //println("query=", query.toList, qid)
            if(roomsBySize(0)(1)<query(1)) {
                answers.addOne((-1, qid))
            }
            else {
                while(i < roomsBySize.size && roomsBySize(i)(1) >= query(1)) {
                    val room = (roomsBySize(i)(0), roomsBySize(i)(1))
                    roomIDSet.add(room)
                    //println("added room to set:", room)
                    i += 1
                }
                val roomBeforeSize = roomIDSet.maxBefore((query(0), query(1)))
                val roomAfterSize = roomIDSet.minAfter((query(0), query(1)))
                val ansRooms: Array[(Int, Int)] = Array(
                    roomBeforeSize.getOrElse((-1, 0)),
                    roomAfterSize.getOrElse((-1, 0))).filter(_._1 != -1).sortBy(_._1)
                //println("ansRooms raw:", ansRooms.toList)
                if(ansRooms.isEmpty)
                    answers.addOne((-1, qid))
                else
                    answers.addOne(
                        (ansRooms.sortBy(_._1).sortBy(t => abs(t._1-query(0)))
                          .map(_._1).reverse.last, qid)
                    )
            }
        }
        answers.toArray.sortBy(_._2).map(_._1)
    }
}
