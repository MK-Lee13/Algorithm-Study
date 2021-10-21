import java.util.*;

class Solution {
  public int solution(String s) {
    int answer = 0;
    HashMap<String, String> map = getMap();
    StringBuffer sr = new StringBuffer();
    StringBuffer aNum = new StringBuffer();
    boolean isNotNum = false;
    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      String s1 = String.valueOf(c);
      if (isNotNum == true && map.containsKey(aNum.toString())) {
        String num = map.get(aNum.toString());
        sr.append(num);
        aNum = new StringBuffer();
      }
      if (map.containsKey(s1)) {
        isNotNum = false;
        sr.append(c);
      } else {
        aNum.append(c);
        isNotNum = true;
      }
    }
    if (isNotNum == true) {
      String num = map.get(aNum.toString());
      sr.append(num);
      aNum = new StringBuffer();
    }
    return Integer.parseInt(sr.toString());
  }

  public HashMap<String, String> getMap() {
    HashMap<String, String> map = new HashMap();
    map.put("zero", "0");
    map.put("one", "1");
    map.put("two", "2");
    map.put("three", "3");
    map.put("four", "4");
    map.put("five", "5");
    map.put("six", "6");
    map.put("seven", "7");
    map.put("eight", "8");
    map.put("nine", "9");
    map.put("0", "0");
    map.put("1", "0");
    map.put("2", "0");
    map.put("3", "0");
    map.put("4", "0");
    map.put("5", "0");
    map.put("6", "0");
    map.put("7", "0");
    map.put("8", "0");
    map.put("9", "0");
    return map;
  }
}