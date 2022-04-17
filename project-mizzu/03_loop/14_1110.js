// [문제]
// [입력] 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
// [출력] 첫째 줄에 N의 사이클 길이를 출력한다.

// [정답]
let input = Number(require('fs').readFileSync('/dev/stdin').toString());

let num = input;
let sum;
let i = 0;

while (true) {
  i++;
  sum = Math.floor(num / 10) + (num % 10);
  num = (num % 10) * 10 + sum % 10;

  if ( input === num ) {
    break;
  }
}

console.log(i);