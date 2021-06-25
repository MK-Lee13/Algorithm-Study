class Solution {
    fun solution(s: String): IntArray {
        var mutableS = s
        var countZero = 0
        var countLoop = 0
        while (mutableS != "1") {
            var length = 0
            var replaceString = ""
            
            for(num in mutableS) {
                if (num == '1') {
                    length += 1
                } else {
                    countZero += 1
                }
            }
            
            while(length > 1) {
                if (length % 2 == 1) {
                    replaceString = "1" + replaceString
                } else {
                    replaceString = "0" + replaceString
                }
                
                length /= 2
            }
            
            if (length == 1) {
                replaceString = "1" + replaceString
            } else {
                replaceString = "0" + replaceString
            }
            
            mutableS = replaceString
            countLoop += 1
        }
        
        return intArrayOf(countLoop, countZero)
    }
}