import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        ArrayList<Integer> line = new ArrayList();
        int max = 0;
        for (int tweight : truck_weights) {
            while (true) {
                if (line.size() == 0) {
                    line.add(tweight);
                    max += tweight;
                    answer += 1;
                    break;
                } else if (line.size() == bridge_length) {
                    max -= line.get(0);
                    line.remove(0);
                } else {
                    if (max + tweight > weight) {
                        line.add(0);
                        answer += 1;
                    } else {
                        line.add(tweight);
                        max += tweight;
                        answer += 1;
                        break;
                    }
                }
            }
        }

        return answer + bridge_length;
    }
}