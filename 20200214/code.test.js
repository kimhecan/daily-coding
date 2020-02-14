function solution(strings, n) {
  return strings.map(v => v[n] + v).sort().map(v => v.substr(1));
}



test('solution', () => {
  expect(solution(['sun', 'bed', 'car'], 1)).toStrictEqual(['car', 'bed', 'sun']);
})

test('solution', () => {
  expect(solution(['abce', 'abcd', 'cdx'], 2)).toStrictEqual(['abcd', 'abce', 'cdx']);
})
