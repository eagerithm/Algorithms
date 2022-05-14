const fs = require("fs");
const inputs = fs.readFileSync(0, "utf-8").toString().split(" ");

const year = parseInt(inputs[0], 10);

if (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) {
  console.log("1");
} else {
  console.log("0");
}
