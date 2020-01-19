object `Reconstruct Itinerary` {
    import scala.collection.mutable.{ArrayBuffer, HashMap, Map, PriorityQueue}

    object Solution {
        def findItinerary(tickets: List[List[String]]): List[String] = {
            val graph = getGraph(tickets)
            // for((k, v) <- graph)
            //     println(k, v)
            val route = ArrayBuffer[String]()
            findItinerary(graph, "JFK", route)
            route.reverse.toList
        }

        def findItinerary(graph: Map[String, PriorityQueue[String]], start: String, route: ArrayBuffer[String]): Unit = {
            //println("start=", start)
            while(!graph(start).isEmpty) {
                val cur = graph(start).dequeue
                findItinerary(graph, cur, route)
            }
            route.append(start)
        }

        def getGraph(tickets: List[List[String]]): Map[String, PriorityQueue[String]] = {
            val ret = HashMap[String, PriorityQueue[String]]()
            for(ticket <- tickets) {
                val (start, end) = (ticket(0), ticket(1))
                if(!ret.contains(start))
                    ret.put(start, PriorityQueue[String]()(scala.math.Ordering[String].reverse))
                if(!ret.contains(end))
                    ret.put(end, PriorityQueue[String]()(scala.math.Ordering[String].reverse))
                ret(start).enqueue(end)
            }
            ret
        }
    }
}
