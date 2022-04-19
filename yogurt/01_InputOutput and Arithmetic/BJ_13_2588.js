// 문제 : (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
//              472 --- (1)
//            x 385 --- (2)
//          -----------------
//             2360 --- (3)
//            3776 ---- (4)
//           1416 ----- (5)
//          -----------------
//           181720 --- (6)

// (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

// 입력 : 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
// 출력 : 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

// 1차 문제 풀이
// const fs = require('fs');
// const [A, B] = fs.readFileSync(0, 'utf8').toString().split('|n');

// const secInput = String(B).split("");

// function settle() {
//   for (let i = secInput.length - 1; i > -1; i--) {
//     console.log(A * secInput[i]);
//   }
//   console.log(A * B);
// }

// settle();

// 첫번째 풀이에 A,B 값을 각각 472, 385를 주어 VSC로 풀이한 결과 출력값은 잘 나왔지만 백준사이트에선 런타임 오류가 일어났다.

// 2차 문제 풀이
const fs = require("fs");
const [A, B] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [B0, B1, B2] = B.split("");

const output1 = parseInt(A * B2);
const output2 = parseInt(A * B1);
const output3 = parseInt(A * B0);
const sum = parseInt(A * B);

console.log(output1);
console.log(output2);
console.log(output3);
console.log(sum);

// for문을 활용하지 않고 배열 B의 각 요소를 가지고와 연산하였다.
