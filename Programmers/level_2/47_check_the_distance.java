import java.util.*;

class Solution {
  public int[] solution(String[][] places) {
    List<Integer> answer = new ArrayList();
    for (int i = 0; i < places.length; i++) {
      if (isValidOnePlace(places[i])) {
        answer.add(1);
      } else {
        answer.add(0);
      }
    }
    return answer.stream().mapToInt(Integer::intValue).toArray();
  }

  public boolean isValidOnePlace(String[] places) {
    for (int i = 0; i < 5; i++) {
      for (int j = 0; j < 5; j++) {
        boolean isValid = true;
        if (places[i].charAt(j) == 'P') {
          isValid = isValidOnePerson(i, j, places);
        }
        if (isValid == false) {
          return isValid;
        }
      }
    }
    return true;
  }

  public boolean isValidOnePerson(int r1, int c1, String[] places) {
    if (r1 + 1 < 5 && places[r1 + 1].charAt(c1) == 'P') {
      return false;
    }
    if (c1 + 1 < 5 && places[r1].charAt(c1 + 1) == 'P') {
      return false;
    }
    if (c1 + 1 < 5 && r1 + 1 < 5 && places[r1 + 1].charAt(c1 + 1) == 'P'
        && (places[r1].charAt(c1 + 1) != 'X' || places[r1 + 1].charAt(c1) != 'X')) {
      return false;
    }

    if (r1 + 1 < 5 && c1 - 1 >= 0 && places[r1 + 1].charAt(c1 - 1) == 'P'
        && (places[r1].charAt(c1 - 1) != 'X' || places[r1 + 1].charAt(c1) != 'X')) {
      return false;
    }

    if (r1 - 2 >= 0 && places[r1 - 2].charAt(c1) == 'P' && places[r1 - 1].charAt(c1) != 'X') {
      return false;
    }
    if (r1 < 3 && places[r1 + 2].charAt(c1) == 'P' && places[r1 + 1].charAt(c1) != 'X') {
      return false;
    }
    if (c1 - 2 >= 0 && places[r1].charAt(c1 - 2) == 'P' && places[r1].charAt(c1 - 1) != 'X') {
      return false;
    }
    if (c1 < 3 && places[r1].charAt(c1 + 2) == 'P' && places[r1].charAt(c1 + 1) != 'X') {
      return false;
    }
    return true;
  }

  public boolean isValid(int r1, int c1, int r2, int c2) {
    int a = r1 - r2;
    int b = c1 - c2;
    if (a < 0)
      a = -a;
    if (b < 0)
      b = -b;
    if (a + b > 2) {
      return true;
    }
    return false;
  }
}