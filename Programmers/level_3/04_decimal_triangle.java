import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int[] copy;
        int[] copy2 = new int[] { triangle[0][0] };
        for (int i = 0; i < triangle.length - 1; i++) {
            copy = copy(triangle[i + 1]);
            for (int j = 0; j < triangle[i].length; j++) {
                int value = copy2[j];
                if (copy[j] < triangle[i + 1][j] + value) {
                    copy[j] = triangle[i + 1][j] + value;
                }
                if (copy[j + 1] < triangle[i + 1][j + 1] + value) {
                    copy[j + 1] = triangle[i + 1][j + 1] + value;
                }
            }
            copy2 = copy;
        }

        Arrays.sort(copy2);

        return copy2[copy2.length - 1];
    }

    public int[] copy(int[] list) {
        int[] result = new int[list.length];
        for (int i = 0; i < list.length; i++) {
            result[i] = 0;
        }
        return result;
    }
}