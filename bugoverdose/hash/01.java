// 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
// 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

// 제한사항
// 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
// completion의 길이는 participant의 길이보다 1 작습니다.
// 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
// 참가자 중에는 동명이인이 있을 수 있습니다.

// 입출력 예
// participant	                                      completion                                return
// ["leo", "kiki", "eden"]                            ["eden", "kiki"]	                        "leo"
// ["marina", "josipa", "nikola", "vinko", "filipa"]  ["josipa", "filipa", "marina", "nikola"]  "vinko"
// ["mislav", "stanko", "mislav", "ana"]	          ["stanko", "ana", "mislav"]	            "mislav"

// 출처: https://hsin.hr/coci/archive/2014_2015/contest2_tasks.pdf

import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> runner_map = new HashMap<String, Integer>();
        String answer = "";
        
        for (String p : participant) {
            if (runner_map.containsKey(p)) {
                runner_map.put(p, runner_map.get(p) + 1);
            } else {
                runner_map.put(p, 1);
            }
        }
        
        for (String c : completion) {
            runner_map.put(c, runner_map.get(c) - 1);
        }
        
        for (String key : runner_map.keySet()){
            if (runner_map.get(key) > 0) {
                answer = key;
            }
        }
        
        return answer;
    }
}

// 다른 사람의 풀이 - getOrDefault
import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String player : participant) hm.put(player, hm.getOrDefault(player, 0) + 1);

        for (String player : completion) hm.put(player, hm.get(player) - 1);

        for (String key : hm.keySet()) {
            if (hm.get(key) != 0){
                answer = key;
            }
        }
        return answer;
    }
}