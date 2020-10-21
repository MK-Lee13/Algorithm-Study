import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        List<Integer> listA = new ArrayList();
        List<Integer> listB = new ArrayList();
        for (int i = 0; i < A.length; i++) {
            listA.add(A[i]);
            listB.add(B[i]);
        }
        while (!listA.isEmpty()) {
            if (listA.get(listA.size() - 1) > listB.get(listB.size() - 1)) {
                answer += listA.get(listA.size() - 1) * listB.get(0);
                listA.remove(listA.size() - 1);
                listB.remove(0);
            } else {
                answer += listB.get(listB.size() - 1) * listA.get(0);
                listB.remove(listB.size() - 1);
                listA.remove(0);
            }
        }
        return answer;
    }
}