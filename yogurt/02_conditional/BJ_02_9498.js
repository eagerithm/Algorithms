// 문제 : 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
// 입력 : 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

// 출력 : 첫째 줄에 다음 세 가지 중 하나를 출력한다.
//        A가 B보다 큰 경우에는 '>'를 출력한다.
//        A가 B보다 작은 경우에는 '<'를 출력한다.
//        A와 B가 같은 경우에는 '=='를 출력한다.

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").toString().trim();

function compare() {
  if (100 >= input && input >= 90) {
    console.log("A");
  } else if (89 >= input && input >= 80) {
    console.log("B");
  } else if (79 >= input && input >= 70) {
    console.log("C");
  } else if (69 >= input && input >= 60) {
    console.log("D");
  } else {
    console.log("F");
  }
}

compare();

// 입력값을 배열로 받아 if 문과 논리연산자 &&(AND)를 활용하여 값을 출력한다.
