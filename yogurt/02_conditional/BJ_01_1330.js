// 문제 : 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
// 입력 : 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

// 출력 : 첫째 줄에 다음 세 가지 중 하나를 출력한다.
//        A가 B보다 큰 경우에는 '>'를 출력한다.
//        A가 B보다 작은 경우에는 '<'를 출력한다.
//        A와 B가 같은 경우에는 '=='를 출력한다.

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").toString().split(" ");

const A = parseInt(input[0]);
const B = parseInt(input[1]);

function compare() {
  if (A > B) {
    console.log(">");
  } else if (A < B) {
    console.log("<");
  } else {
    console.log("==");
  }
}
compare();

// 입력값을 배열로 받아 if 문을 활용하여 원하는 등호를 출력한다.
