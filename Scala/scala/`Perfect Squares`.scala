object `Perfect Squares` {
    object Solution {
        def numSquares(n: Int): Int = {
            val sqs = Array.fill(n + 1){n}
            sqs(0) = 0
            for(cur <- 1 to n) {
                for(x <- 1 to cur if x*x <= cur)
                    sqs(cur) = math.min(sqs(cur), 1 + sqs(cur - x*x))
            }
            sqs.last
        }
    }
}
