class Solution {
  fun solution(s: String): Int {
      var answer = 1
      for (i in s.indices) {
          var value = palindromMatcherForLoop(s, i)
          if (value > answer) {
              answer = value
          }
          
          if (answer == s.length - i) {
              return answer
          }
      }
      return answer
  }
  
  fun palindromMatcherForLoop(s: String, start: Int): Int {
      for (end in s.length - 1 downTo start + 1) {
          if (checkPalindrom(s, start, end) == true) {
              return (end - start) + 1 
          }
      }
      return 0
  }
  
  fun checkPalindrom(s: String, start: Int, end: Int): Boolean {
      var length = end + 1
      var middleLength = (length - start) / 2
      for (i in 0..middleLength - 1) {
          var base = start + i
          if (s[base] != s[length - 1 - i]) {
              return false
          }
      }
      return true
  }
}