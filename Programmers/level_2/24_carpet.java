import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        ArrayList<XY> pairs = returnPairs(brown + yellow);
        for (XY pair : pairs) {
            int x = pair.getX();
            int y = pair.getY();
            int compare = ((y - 2) * (x - 2));
            if (yellow == compare) {
                return new int[] {x, y};
            }
        }
        
        return answer;
    }
    
    public ArrayList<XY> returnPairs(int total) {
        ArrayList<XY> pairs = new ArrayList();
        for (int i = 3; i < (total / 2); i++) {
            if (total % i == 0) {
                pairs.add(new XY(total / i, i));
            }
        }
        return pairs;
    }
}

class XY {
    int x;
    int y;
    
    public XY(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public int getX() {
        return this.x;
    }
    
    public int getY() {
        return this.y;
    }
}