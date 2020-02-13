function solution(n) {
  let answer = 0;
  for(let i=1; i<=n; i++) {
    if(n % i == 0) answer += i
  }
  return answer;
}


test('solution', () => {
  expect(solution(12)).toBe(28)
});

test('solution', () => {
  expect(solution(5)).toBe(6)
});

