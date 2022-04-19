// 문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
// 입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
// 출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

const fs = require("fs");
const inputData = fs.readFileSync(0, "utf8").toString().split(" ");

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

console.log(A + B);
console.log(A - B);
console.log(A * B);
console.log(Math.floor(A / B));
console.log(A % B);

// 입력값을 배열로 A와 B를 사칙연산하면 된다.
// 단 A/B는 정수로 반환하여야 정답처리가 되므로 Math.floor를 사용해야한다.
