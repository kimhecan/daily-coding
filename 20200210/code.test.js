function solution(s) {
  return s.split('').sort().reverse().join('');
}

test('solution', () => {
  expect('abc').toBe('cba')
});

test('solution', () => {
  expect('Zbcdefg').toBe('gfedcbZ')
})