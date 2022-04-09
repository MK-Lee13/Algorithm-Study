import java.util.*;

class Solution {
  public int[] solution(int m, int n, int[][] picture) {
    int numberOfArea = 0;
    int maxSizeOfOneArea = 0;

    int[][] copy = new int[picture.length][picture[0].length];
    for (int i = 0; i < copy.length; i++) {
      copy[i] = picture[i].clone();
    }

    for (int y = 0; y < m; y++) {
      for (int x = 0; x < n; x++) {
        if (copy[y][x] != 0) {
          numberOfArea += 1;
          int isMax = bfs(y, x, copy, m, n);
          maxSizeOfOneArea = Math.max(maxSizeOfOneArea, isMax);
        }
      }
    }

    int[] answer = new int[2];
    answer[0] = numberOfArea;
    answer[1] = maxSizeOfOneArea;
    return answer;
  }

  public int bfs(int y, int x, int[][] picture, int m, int n) {
    int target_color = picture[y][x];
    int answer = 0;
    HashMap<String, Integer> recursiveTable = new LinkedHashMap<>();
    Queue<Position> queue = new LinkedList<>();
    queue.add(new Position(y, x));

    while (queue.size() != 0) {
      Position node = queue.poll();
      int nextX = node.getX();
      int nextY = node.getY();
      picture[nextY][nextX] = 0;
      answer += 1;
      putKey(nextY, nextX, recursiveTable);

      if (nextX - 1 >= 0 && picture[nextY][nextX - 1] == target_color && isValidKey(nextY, nextX - 1, recursiveTable)) {
        queue.add(new Position(nextY, nextX - 1));
        putKey(nextY, nextX - 1, recursiveTable);
      }
      if (nextY - 1 >= 0 && picture[nextY - 1][nextX] == target_color && isValidKey(nextY - 1, nextX, recursiveTable)) {
        queue.add(new Position(nextY - 1, nextX));
        putKey(nextY - 1, nextX, recursiveTable);
      }
      if (nextX + 1 < n && picture[nextY][nextX + 1] == target_color && isValidKey(nextY, nextX + 1, recursiveTable)) {
        queue.add(new Position(nextY, nextX + 1));
        putKey(nextY, nextX + 1, recursiveTable);
      }
      if (nextY + 1 < m && picture[nextY + 1][nextX] == target_color && isValidKey(nextY + 1, nextX, recursiveTable)) {
        queue.add(new Position(nextY + 1, nextX));
        putKey(nextY + 1, nextX, recursiveTable);
      }
    }
    return answer;
  }

  private void putKey(int y, int x, HashMap<String, Integer> recursiveTable) {
    recursiveTable.put(String.format("%d-%d", y, x), 1);
  }

  private boolean isValidKey(int y, int x, HashMap<String, Integer> recursiveTable) {
    return !recursiveTable.containsKey(String.format("%d-%d", y, x));
  }

  public class Position {
    int x;
    int y;

    public Position(int y, int x) {
      this.x = x;
      this.y = y;
    }

    public int getX() {
      return x;
    }

    public int getY() {
      return y;
    }
  }
}