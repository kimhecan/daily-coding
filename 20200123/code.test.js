/* 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다. */

function solution(a, b) {
  let answer = 0;
  if (a < b) {
    while ( a <= b) {
      answer += a;
      a += 1;
    };
  } else if (a > b) {
    while ( b <= a) {
      answer += b;
      b += 1;
    };
  } else {
    answer = a;
  }
  return answer;
}




test('solution', () => {
  expect(solution(3, 5)).toBe(12);
});

test('solution', () => {
  expect(solution(5, 3)).toBe(12);
});

test('solution', () => {
  expect(solution(3, 3)).toBe(3);
});

