object `Binary Watch` {
    object Solution {
        def readBinaryWatch(num: Int): List[String] = {
            val hMap = Array(Array("0"), Array("1", "2", "4", "8"), Array("3", "5", "6", "9", "10"), Array("7", "11"))
            val mMap = Array(Array("00"), Array("01", "02", "04", "08", "16", "32"),
                Array("03", "05", "06", "09", "10", "12", "17", "18", "20", "24", "33", "34", "36", "40", "48"),
                Array("07", "11", "13", "14", "19", "21", "22", "25", "26", "28", "35", "37", "38", "41", "42", "44", "49", "50", "52", "56"),
                Array("15", "23", "27", "29", "30", "39", "43", "45", "46", "51", "53", "54", "57", "58"), Array("31", "47", "55", "59"))

            var ret = List[String]()
            for (i <- 0 to num if i < hMap.length && num - i < mMap.length) {
                ret = ((for {h <- hMap(i); m <- mMap(num - i)}
                    yield s"${h}:${m}").toList) ++ ret
            }
            ret
        }
    }
}
