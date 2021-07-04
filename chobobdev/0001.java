// 1 번 답안
class Solution {
  public String solution(int n) {
      String answer = "";
      String watermel = "수박";
      if(n%2==0){
          answer=watermel.repeat(n/2);
      }
      else{
          answer=watermel.repeat(n/2)+"수";
      }
      return answer;
  }
}