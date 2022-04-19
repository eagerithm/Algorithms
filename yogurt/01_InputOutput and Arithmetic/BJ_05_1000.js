// 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
// 입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
// 출력 : 첫째 줄에 A+B를 출력한다.

const fs = require("fs");
const inputData = fs.readFileSync(0, "utf8").toString().split(" ");

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

console.log(A + B);

// 입력값을 배열로 받아 배열의 [0] + [1]을 해준다.

// * 백준 사이트의 컴파일 실행 도움말에서 Node.js의 입력 받는 법이 있다.
//   이에 관련된 블로그 글을 참조함
//   https://overcome-the-limits.tistory.com/25
