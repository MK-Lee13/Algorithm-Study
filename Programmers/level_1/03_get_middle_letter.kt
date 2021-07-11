class Solution {
    fun solution(s: String): String {
        var answer = ""
        var base = (s.length / 2).toInt()
        if (s.length == 1 || s.length == 2) {
            return s
        }
        
        if (s.length % 2 == 0) {
            return s.substring(base - 1, base + 1)
        } else {
            return s.substring(base, base + 1)
        }
    }
}