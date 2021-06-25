class Solution {
    fun solution(s: String): String {
        var answer = ""
        val matchRegex = "([a-z])".toRegex()
        var isFirstOfString = true
        for (s1 in s) {
            if (isFirstOfString == true) {
                answer += s1.toUpperCase()
                isFirstOfString = false
                
                if (s1 == ' ') {
                    isFirstOfString = true
                }
                
                continue
            }
            
            answer += s1.toLowerCase()
            
            if (s1 == ' ') {
                isFirstOfString = true
            }
            
        }
        return answer
    }
}