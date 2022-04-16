// [입력] 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 
// 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
// [출력] 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

// [정답]
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let T = parseInt(input[0]);
let answer = "";

for ( let i = 1; i <= T; i++ ) {
  let nums = input[i].split(" ");
  answer += parseInt(nums[0]) + parseInt(nums[1]) + "\n";
}

console.log(answer);