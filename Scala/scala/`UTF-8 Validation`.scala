object `UTF-8 Validation` {
    object Solution {
        def validUtf8(data: Array[Int]): Boolean = {
            var cur = 0
            while(cur < data.size) {
                cur = validate(data, cur)
                if(cur < 0)
                    return false
            }
            cur >= 0
        }

        private def validate(data: Array[Int], start: Int): Int = {

            val startswith10 = (num: Int) => (0xC0 & (~(num ^ 0x80))) == 0xC0

            if((data(start) & 0x80) == 0) {
                start + 1
            }
            else if((0xE0 & (~(data(start) ^ 0xC0))) == 0xE0) {
                if(start+1 < data.size && startswith10(data(start + 1)))
                    start + 2
                else
                    -1
            }
            else if((0xF0 & (~(data(start) ^ 0xE0))) == 0xF0) {
                if(start+2 < data.size && startswith10(data(start + 1)) && startswith10(data(start + 2)))
                    start + 3
                else
                    -1
            }
            else if((0xF8 & (~(data(start) ^ 0xF0))) == 0xF8) {
                if(start+3 < data.size &&
                  startswith10(data(start + 1)) &&
                  startswith10(data(start + 2)) &&
                  startswith10(data(start + 3)))
                    start + 4
                else
                    -1
            }
            else
                -1
        }
    }


}
