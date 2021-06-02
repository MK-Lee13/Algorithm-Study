import java.util.*;

class Solution {
    public String solution(String s) {
        String[] listOfString = s.split(" ");
        int max = Integer.parseInt(listOfString[0]);
        int min = max;
        for (String str : listOfString) {
            int value = Integer.parseInt(str);
            if (min > value) {
                min = value;
            }

            if (max < value) {
                max = value;
            }
        }
        return min + " " + max;
    }
}