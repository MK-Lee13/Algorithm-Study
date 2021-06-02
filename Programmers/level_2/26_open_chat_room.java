import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        ArrayList<String> answer = new ArrayList<>();
        HashMap<String, String> userList = new HashMap<>();
        
        for (String reco : record) {
            String[] splitReco = reco.split(" ");
            if (splitReco.length == 3) {
               checker(splitReco[1], splitReco[2], userList);
            }
        }
        
        for (String reco : record) {
            String[] splitReco = reco.split(" ");
            String name = returnName(splitReco[1], userList);
            
            if (splitReco[0].equals("Enter")) {
                answer.add(name + "님이 들어왔습니다.");
            } else if (splitReco[0].equals("Leave")) {
                answer.add(name + "님이 나갔습니다.");
            }
        }
        
        return answer.toArray(new String[answer.size()]);
    }
    
    public String returnName(String uid, HashMap<String, String> userList) {
        return userList.get(uid);
    }
    
    public void checker(String uid, String name, HashMap<String, String> userList) {
        userList.put(uid, name);
    }
}