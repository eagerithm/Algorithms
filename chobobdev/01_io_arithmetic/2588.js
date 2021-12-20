var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().split('\n')
var a = parseInt(input[0])
var b = parseInt(input[1])
var c = b + ''
console.log(a*c.substr(2,1))
console.log(a*c.substr(1,1))
console.log(a*c.substr(0,1))
console.log(a*c.substr(0,3))