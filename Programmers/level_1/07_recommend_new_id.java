import java.util.regex.*;
import java.util.*;

class Solution {
    public String solution(String new_id) {
        new_id = new_id.toLowerCase();
        String s = new_id.replaceAll("[~!@#$%^&*\\(\\)=+\\[\\{\\]\\}:?,<>/]","");
        String next = s;
        int current_size = next.length();
        int next_size = 0;
        while (current_size != next_size) {
            current_size = next_size;
            next = checkAndRemovePoint(next);
            next_size = next.length();
        }
        next = sizeReplace(next);
        return next;
    }
    
    public String sizeReplace(String s) {
        StringBuffer sizeString = new StringBuffer(s);
        while (sizeString.length() > 15 || sizeString.length() < 3) {
            if (sizeString.length() == 0) {
                sizeString.append('a');
            } else if (sizeString.charAt(sizeString.length() - 1) == '.') {
                sizeString.deleteCharAt(sizeString.length() - 1);
            } else if (sizeString.length() > 15) {
                sizeString.deleteCharAt(sizeString.length() - 1);
            } else if (sizeString.length() < 3) {
                sizeString.append(sizeString.charAt(sizeString.length() - 1));
            }
        }
        if (sizeString.charAt(sizeString.length() - 1) == '.') {
            sizeString.deleteCharAt(sizeString.length() - 1);
        } 
        return sizeString.toString();
    }
    
    public String checkAndRemovePoint(String s) {
        StringBuffer pointString = new StringBuffer();
        boolean findPoint = false;
        for (int i = 0; i < s.length(); i++) {
            if (i == 0 && s.charAt(i) == '.') continue;
            if (i + 1 == s.length() && s.charAt(i) == '.') continue;
            if (s.charAt(i) == '.') {
                findPoint = true;
                continue;
            }
            if (findPoint == true && s.charAt(i) != '.') {
                pointString.append('.');
            }
            pointString.append(s.charAt(i));
            findPoint = false;
        }
        return pointString.toString();
    }
}