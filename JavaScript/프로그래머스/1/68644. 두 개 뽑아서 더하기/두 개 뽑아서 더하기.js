function solution(numbers) {
  let answer = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < i; j++) {
      const number = numbers[i] + numbers[j];
      answer.push(number);
    }
  }
  let newSet = new Set(answer);
  let newAnswer = [...newSet].sort((a, b) => a - b);

  return newAnswer;
}