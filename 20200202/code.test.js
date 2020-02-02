function solution(s){
  let string = s.toLowerCase().split("");
  let pOnly = string.filter(v => v == "p");
  let yOnly = string.filter(v => v == "y");

  return pOnly.length == yOnly.length ? true : false;
}


test('solution', () => {
  expect(solution("pPoooyY")).toBe(true)
});

test('solution', () => {
  expect(solution("Pyy")).toBe(false)
});
