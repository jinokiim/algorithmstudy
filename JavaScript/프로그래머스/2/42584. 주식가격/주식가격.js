function solution(prices) {
  let answer = [];

  for (let i = 0; i < prices.length; i++) {
    let price = prices[i];
    let count = 0;
    for (let t = i + 1; t < prices.length; t++) {
      count += 1;
      if (price > prices[t]) {
        break;
      }
    }
    answer.push(count);
  }

  return answer;
}