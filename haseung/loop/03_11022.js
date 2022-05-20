const fs = require("fs");
const testCase = fs.readFileSync(0, "utf-8").toString().split("\n");

for (let i = 1; i <= testCase[0]; i++) {
  let result = testCase[i].split(" ");

  let num1 = Number(result[0]);
  let num2 = Number(result[1]);

  console.log(`Case #${i}: ${num1} + ${num2} = ${num1 + num2}`);
}
