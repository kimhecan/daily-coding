function solution(arr, divisor) {

  let answer = arr.filter(v => v % divisor == 0)
  answer.length === 0 ? answer.push(-1) : answer

  return answer.sort((a, b) => a - b)
}




test('solution', () => {
  expect(solution([5, 9, 7, 10],5)).toStrictEqual([5, 10])
});

test('solution', () => {
  expect(solution([2, 36, 1, 3],1)).toStrictEqual([1, 2, 3, 36])
});

test('solution', () => {
  expect(solution([3,2,6],10)).toStrictEqual([-1])
});