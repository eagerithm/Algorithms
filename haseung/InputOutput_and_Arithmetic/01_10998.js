const fs = require("fs");
const inputs = fs.readFileSync(0, "utf-8").toString().split(" ");

const a = parseInt(inputs[0], 10);
const b = parseInt(inputs[1], 10);

console.log(a * b);
