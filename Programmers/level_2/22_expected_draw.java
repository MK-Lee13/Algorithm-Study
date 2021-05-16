import java.util.*;

class Solution {
    public int solution(int n, int a, int b) {
        int answer = 1;
        while (check(a, b)) {
            if (a % 2 == 0) {
                a = a / 2;
            } else {
                a = (a + 1) / 2;
            }

            if (b % 2 == 0) {
                b = b / 2;
            } else {
                b = (b + 1) / 2;
            }
            answer += 1;
        }
        return answer;
    }

    public Boolean check(int a, int b) {
        if (a % 2 == 0 && a == b + 1) {
            return false;
        } else if (b % 2 == 0 && b == a + 1) {
            return false;
        }

        return true;
    }
}