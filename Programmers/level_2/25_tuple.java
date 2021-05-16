import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer;
        ArrayList<String[]> list = spliter(s);
        ArrayList<Integer> answer_list = new ArrayList();
        
        list.sort(new Comparator<String[]>() { 
            @Override
            public int compare(String[] b1, String[] b2) { 
                return b1.length - b2.length; 
            } 
        });
        
        for (String[] column : list) {
            answer_list.add(check(column, answer_list));
        }
        
        answer = new int[answer_list.size()];
        
        for (int i = 0; i < answer_list.size(); i++) {
            answer[i] = answer_list.get(i);
        }
        
        return answer;
    }
    
    public ArrayList<String[]> spliter(String s) {
        String first = s.substring(1, s.length() - 1);
        String[] second = first.split("},");
        ArrayList<String[]> result = new ArrayList<String[]>();
        
        for (String s_a : second) {
            String third = s_a.replace("{","");
            third = third.replace("}", "");
            String[] last = third.split(",");
            result.add(last);
        }
        
        return result;
    }
    
    public int check(String[] column, ArrayList<Integer> answer_list) {
        if (answer_list.size() == 0) {
            return Integer.parseInt(column[0]);
        }
        
        for (int i = 0; i < column.length; i++) {
            Boolean check = false;
            int value = Integer.parseInt(column[i]);
            for (int j = 0; j < answer_list.size(); j++) {
                if (value == answer_list.get(j)) {
                    check = true;
                    break;
                }
            }
            if (check == false) {
                return value;
            }
        }
        
        return 0;
    }
}