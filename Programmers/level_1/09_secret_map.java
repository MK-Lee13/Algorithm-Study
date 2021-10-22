import java.util.*;

class Solution {
  public String[] solution(int n, int[] arr1, int[] arr2) {
    String[] answer = new String[n];
    for (int i = 0; i < arr1.length; i++) {
      int num = arr1[i] | arr2[i];
      answer[i] = makeString(num, n);
    }
    return answer;
  }

  public String makeString(int num, int n) {
    String s = "";
    while (num > 1) {
      if (num % 2 == 1) {
        s = "#" + s;
      } else {
        s = " " + s;
      }
      num /= 2;
    }
    if (num == 1) {
      s = "#" + s;
    } else {
      s = " " + s;
    }
    while (s.length() < n) {
      s = " " + s;
    }
    return s;
  }
}