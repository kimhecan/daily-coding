function solution(s) {
  let splitArr = s.split(" ");
  return splitArr.map(v => (v.split("").map((v, i) => i % 2 === 0 ? v.toUpperCase() : v.toLowerCase())).join("")).join(" ");
}

test('solution', () => {
  expect(solution("try hello world")).toBe("TrY HeLlO WoRlD")
});
