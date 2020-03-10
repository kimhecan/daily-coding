function solution(departList, budget) {
  departList.sort();
  let sum = 0;

  for(let i=0; i<departList.length; i++) {
    sum += departList[i];
    if (sum > budget) return i
    if (sum == budget) return i+1
    if (i == departList.length - 1) return departList.length 
  }
}


// function solution(d, budget) {
//   d.sort((a, b) => a - b);

//   while (d.reduce((a, b) => (a + b), 0) > budget) d.pop();

//   return d.length;
// }


test('solution', () => {
  expect(solution([1,1], 3)).toBe(2)
  expect(solution([2,3,4,5], 1)).toBe(0)
  expect(solution([1,1,1,1], 3)).toBe(3)
  expect(solution([1,1,1,1,1], 4)).toBe(4)
  expect(solution([1,3,2,5,4], 9)).toBe(3)
  expect(solution([2,2,3,3], 13)).toBe(4)
});