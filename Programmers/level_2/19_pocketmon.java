import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        TreeSet<Integer> treeSet = new TreeSet<>();
        for(int data : nums){
            treeSet.add(data);
        }
        if (nums.length / 2 > treeSet.size()) {
            return treeSet.size();
        } else {
            return nums.length / 2;
        }
    }
}