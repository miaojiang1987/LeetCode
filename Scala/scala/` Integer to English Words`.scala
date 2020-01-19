object ` Integer to English Words` {
    object Solution {
        val one2twenty = Array[String](
            "", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        )
        val twenty2ninety = Array[String](
            "", //0
            "", // 1
            "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        )
        def numberToWords(num: Int): String = {
            if(num == 0)
                return "Zero"
            var cur = num
            val triplet_names = Array[String]("Billion", "Million", "Thousand", "")
            var triplets = List[String]()
            for(_ <- 0 until 4) {
                triplets = decodeTriplet(cur % 1000)::triplets
                cur /= 1000
            }
            val ret = new StringBuilder()
            for(tname <- triplet_names) {
                if(triplets.head != "") {
                    ret.append(triplets.head + ' ' + tname + ' ')
                }
                triplets = triplets.tail
            }
            ret.toString.trim
        }

        private def decodeTriplet(num: Int): String = {
            // println("triplet:", num)
            val ret = new StringBuilder()
            var cur = num
            if(cur / 100 > 0) {
                ret.append(s"${one2twenty(cur/100)} Hundred ")
            }
            cur %= 100
            if(cur < 20) {
                ret.append(s"${one2twenty(cur)}")
            }
            else {
                ret.append(s"${twenty2ninety(cur/10)} ")
                cur %= 10
                ret.append(s"${one2twenty(cur)}")
            }
            ret.toString.trim
        }
    }
}
