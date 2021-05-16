import java.util.*;

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        // 2*3 3* 4 = 1* 4
        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr2[0].length; j++) {
                answer[i][j] = calc(arr1, arr2, i, j);
            }
        }
        return answer;
    }

    public int calc(int[][] arr1, int[][] arr2, int x, int y) {
        int result = 0;
        for (int i = 0; i < arr2.length; i++) {
            result += arr1[x][i] * arr2[i][y];
        }
        return result;
    }
}