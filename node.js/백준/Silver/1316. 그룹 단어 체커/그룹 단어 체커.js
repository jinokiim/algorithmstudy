let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");


function solution(array) {
  let answer = 0;

  let inputCount = array[0];
  array.shift();

  for (let i = 0; i < inputCount; i++) {
    let word = array[i];
    let trash = [];
    let status = true;
    // happy
    for (let j = 0; j < word.length; j++) {
      let letter = word[j];
      // h
      if (!trash.includes(letter)) {
        trash.push(letter);
      } else if (letter !== word[j - 1]) {
        status = false;
        break;
      }
    }
    if (status) answer++;
  }

  console.log(answer);
}

solution(input);
