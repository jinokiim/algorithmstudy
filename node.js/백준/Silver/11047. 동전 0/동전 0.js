const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


const [N, K] = input[0].split(" ").map(Number);

const coins = input.slice(1).map(Number).reverse();

let answer = 0;
let tempValue = K;

for (let i = 0; i < N; i++) {
  const coin = coins[i];

  if (tempValue >= coin) {
    const count = parseInt(tempValue / coin);
    tempValue = tempValue - coin * count;
    answer = answer + count;

    if (tempValue === 0) break;
  }
}

console.log(answer);
