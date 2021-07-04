import java.util.*;

class Solution {
    public int solution(String s) {
        String[] s_split = s.split("");
        ArrayList<String> first_stack = new ArrayList<String>();
        first_stack.add(s_split[0]);
        for (int i = 1; i < s_split.length; i += 1) {
            int last_stack_index = first_stack.size() - 1;
            String next = s_split[i];

            if (first_stack.size() == 0) {
                first_stack.add(next);
                continue;
            }

            String first = first_stack.get(last_stack_index);

            if (first.equals(next)) {
                first_stack.remove(last_stack_index);
            } else {
                first_stack.add(next);
            }
        }

        if (first_stack.size() != 0) {
            return 0;
        }

        return 1;
    }
}