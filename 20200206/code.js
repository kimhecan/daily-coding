function solution(answers) {
  let answer = [];
  
  let a1 = [1, 2, 3, 4, 5];
  let a2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let a1c = answers.filter((a, i) => a === a1[i%a1.length]).length;
  let a2c = answers.filter((a, i) => a === a2[i%a2.length]).length;
  let a3c = answers.filter((a, i) => a === a3[i%a3.length]).length;

  let max = Math.max(a1c, a2c, a3c);

  if (a1c === max) {answer.push(1)}
  if (a2c === max) {answer.push(2)}
  if (a3c === max) {answer.push(3)}

  return answer

}


console.log(solution([1,2,3,4,5]));
console.log(solution([1,3,2,4,2]));

// 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5 
// index % 2 == 0  => 2
// index % 2 == 1 => 
// 1 => index % 8 = 1
// 3 => index % 8 = 3
// 4 => (index % 8) -1 = 4
// 5 => (index % 8) = 7 
// 1 1
// 3 3
// 5 4
// 7 5
// 9 1
// 11 3
// 13 4
// 15 5
// 17 1
// 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5

//01 index % 10 = => 3
//23 index % 10 = => 1
//45 index % 10 = => 2
//67 index % 10 = => 4
//89 index % 10 = => 5