import java.util.*;

class Solution {
    public String solution(String number, int k) {
        StringBuilder numList = new StringBuilder(number);
        int start = 0;
        int popCount = 0;
        while (k > popCount && start != numList.length() - 1) {
            if (numList.charAt(start) < numList.charAt(start + 1)) {
                numList.deleteCharAt(start);
                popCount ++;
                start -= 1;
                if (start < 0) start = 0;
            } else {
                start += 1;
            }
        }
        if (number.length() - k < numList.length()) {
            return String.join("", numList.substring(0, number.length() - k));
        } else {
            return String.join("", numList);
        }
    }
}