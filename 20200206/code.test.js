function solution(answers) {

  let answer = [];
  
  let v1 = [1, 2, 3, 4, 5];
  let v2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let v3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let scores = [0, 0, 0];

  scores[0] = answers.filter((v, i) => v === v1[i % v1.length]).length;
  scores[1] = answers.filter((v, i) => v === v2[i % v2.length]).length;
  scores[2] = answers.filter((v, i) => v === v3[i % v3.length]).length;

  let max = Math.max(scores[0],scores[1],scores[2]);

  if (scores[0] === max) answer.push(1);
  if (scores[1] === max) answer.push(2);
  if (scores[2] === max) answer.push(3);

  return answer
}

test('solution', () => {
  expect(solution([1,2,3,4,5])).toStrictEqual([1])
});

test('solution', () => {
  expect(solution([1,3,2,4,2])).toStrictEqual([1,2,3])
});