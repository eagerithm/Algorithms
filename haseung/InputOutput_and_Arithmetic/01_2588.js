const fs = require("fs");
const inputs = fs.readFileSync(0, "utf-8").toString().split("\n");

const a = parseInt(inputs[0], 10);
const b = parseInt(inputs[1], 10);

const c = b % 10;
const d = Math.floor((b % 100) / 10);
const e = Math.floor(b / 100);

console.log(a * c);
console.log(a * d);
console.log(a * e);
console.log(a * b);
