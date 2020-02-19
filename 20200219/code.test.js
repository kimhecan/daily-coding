function solution(n, m) {
  let mul = n * m;
  while ( m !== 0) {
    r = n % m;
    n = m;
    m = r;
  }
  return [n, mul / n]
}



test('solution', () => {
  expect(solution(3, 12)).toStrictEqual([3,12])
});

test('solution', () => {
  expect(solution(2, 5)).toStrictEqual([1,10])
});