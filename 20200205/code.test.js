function solution(a, b) {
  let date = new Date(`2016-${a}-${b}`).getDay();
  let dayList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

  return dayList[date]
}


test('solution', () => {
  expect(solution(1,1)).toBe("FRI")
})

test('solution', () => {
  expect(solution(5, 24)).toBe("TUE")
});