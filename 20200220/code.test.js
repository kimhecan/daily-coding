function solution(x) {
  const sum = String(x).split('').reduce((acc, cur) => acc + +cur, 0)
  return x % sum === 0 ? true : false
}


test('solution', () => {
  expect(solution(10)).toBe(true)
})

test('solution', () => {
  expect(solution(12)).toBe(true)
})

test('solution', () => {
  expect(solution(11)).toBe(false)
})

test('solution', () => {
  expect(solution(13)).toBe(false)
})
