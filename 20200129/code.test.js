function solution(arr) {
  let answer = 0;
  for(let i=0; i<arr.length; i++) {
    answer += arr[i];
  }
  answer = answer / arr.length;
  return answer;
}



test('solution', () => {
  expect(solution([1,2,3,4])).toBe(2.5);
});

test('solution', () => {
  expect(solution([5,5])).toBe(5);
});