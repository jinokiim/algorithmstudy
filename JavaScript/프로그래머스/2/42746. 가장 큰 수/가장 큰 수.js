function solution(numbers) {
  let answer = "";
  // console.log("numbers.sort()", numbers.sort());
  // console.log("numbers.sort().reverse", numbers.sort().reverse());
  // const desc = a.sort((a,b)=>(b-a));

  const sortedArray = numbers.sort(
    (a, b) => String(b) + String(a) - (String(a) + String(b))
  );

  answer = sortedArray.join("");
  return Number(answer) === 0 ? "0" : answer;
}
