const fs = require("fs");
const inputs = fs.readFileSync(0, "utf-8").toString().split("\n");

const a = parseInt(inputs[0], 10);
const b = parseInt(inputs[1], 10);

if (a > 0 && b > 0) {
  console.log("1");
} else if (a < 0 && b > 0) {
  console.log("2");
} else if (a < 0 && b < 0) {
  console.log("3");
} else {
  console.log("4");
}
