const fs = require("fs");
const inputs = fs.readFileSync(0, "utf-8").toString().split(" ");

const a = parseInt(inputs[0], 10);
const b = parseInt(inputs[1], 10);
const c = parseInt(inputs[2], 10);

console.log(Number((a + b) % c));
console.log(Number(((a % c) + (b % c)) % c));
console.log(Number((a * b) % c));
console.log(Number(((a % c) * (b % c)) % c));
