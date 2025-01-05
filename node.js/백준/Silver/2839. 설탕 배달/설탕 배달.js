const fs = require("fs");

const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim(), 10);

let answer = -1;

if (input % 5 === 0) {
  answer = input / 5;
} else {
  for (let i = 0; i <= Math.floor(input / 3); i++) {
    if ((input - i * 3) % 5 === 0) {
      answer = i + Math.floor((input - i * 3) / 5);
      break;
    }
  }
}

console.log(answer);
