class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        Boolean[] isVisted = new Boolean[n];
        clearisVisited(isVisted);
        for (int i = 0; i < n; i++) {
            if (isVisted[i] == false) {
                dfs(i, isVisted, computers);
                answer += 1;
            }
        }
        return answer;
    }

    public void dfs(int index, Boolean[] isVisted, int[][] computers) {
        isVisted[index] = true;
        for (int i = 0; i < isVisted.length; i++) {
            if (computers[index][i] == 1 && isVisted[i] == false) {
                dfs(i, isVisted, computers);
            }
        }
    }

    public void clearisVisited(Boolean[] isVisted) {
        for (int i = 0; i < isVisted.length; i++) {
            isVisted[i] = false;
        }
    }
}