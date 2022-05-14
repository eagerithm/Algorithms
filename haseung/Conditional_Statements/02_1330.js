//두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

const fs = require("fs");
const inputs = fs.readFileSync(0, "utf-8").toString().split(" ");

const a = parseInt(inputs[0], 10);
const b = parseInt(inputs[1], 10);

if (a === b) {
  console.log("==");
} else if (a > b) {
  console.log(">");
} else {
  console.log("<");
}
