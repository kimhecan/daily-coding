function solution(departList, budget) {
  departList.sort();
  let sum = 0;

  for(let i=0; i<departList.length; i++) {
    sum += departList[i];
    if (sum > budget) return i
    if (sum == budget) return i+1
  }
}

test('solution', () => {
  expect(solution([1], 1)).toBe(1)
  expect(solution([2,3,4,5], 1)).toBe(0)
  expect(solution([1,1,1,1], 3)).toBe(3)
  expect(solution([1,1,1,1,1], 5)).toBe(5)
  expect(solution([1,3,2,5,4], 9)).toBe(3)
  expect(solution([2,2,3,3], 10)).toBe(4)
});