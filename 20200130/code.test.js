function solution(s) {
  let regEx = /^\d{4,4}$|^\d{6,6}$/;
  let result = s.match(regEx);
  let answer = result == null ? false : true
  return answer;
}


test('solution', () => {
  expect(solution("a234")).toBe(false)
});

test('solution', () => {
  expect(solution("1234")).toBe(true)
});