function solution(n) {
  
  let count = 0;
  while(n !== 1) {
    if (n % 2 == 0) n /= 2;
    else n = n*3 + 1;
    count++
    if (count == 500) return -1
  };
  return count
  
};


test('solution', () => {
  expect(solution(6)).toBe(8)
});

test('solution', () => {
  expect(solution(16)).toBe(4)
});

test('solution', () => {
  expect(solution(626331)).toBe(-1)
});