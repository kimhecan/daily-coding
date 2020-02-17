function solution(n) {
  return Number.isInteger(Math.sqrt(n)) ? Math.pow(Math.sqrt(n)+1,2) : -1
}

test('solution', () => {
  expect(solution(121)).toBe(144);
})

test('solution', () => {
  expect(solution(3)).toBe(-1);
})