function solution(s) {
  
  return Number(s);
}



test('solution', () => {
  expect(solution("+123")).toBe(123)
});

test('solution', () => {
  expect(solution("-123")).toBe(-123)
});