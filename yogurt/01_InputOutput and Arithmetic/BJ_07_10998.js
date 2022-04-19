// 문제 : 두 정수 A와 B를 입력받은 다음, AxB를 출력하는 프로그램을 작성하시오.
// 입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
// 출력 : 첫째 줄에 AxB를 출력한다.

const fs = require("fs");
const inputData = fs.readFileSync(0, "utf8").toString().split(" ");

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

console.log(A * B);

// 입력값을 배열로 받아 배열의 [0] x [1]을 해준다.
