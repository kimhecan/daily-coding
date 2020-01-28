function solution(arr) {
  let answer = [arr[0]];
  for (let i=1; i < arr.length; i++) {
    if (arr[i] == arr[i-1]) {
      continue;
    };
    answer.push(arr[i])
  }
  return answer
}


test('solution', () => {
  expect(solution([1,1,3,3,0,1,1])).toStrictEqual([1,3,0,1]);
});

test('solution', () => {
  expect(solution([4,4,4,3,3])).toStrictEqual([4,3]);
});

