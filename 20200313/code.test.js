function solution(n, stages) {
  let arr = [];

  // 각 스테이지의 실패율 구하기
  for(let i=1; i<=n; i++) {
    arr.push({'stageNumber': i, 'failRate': stages.filter(v => v === i).length / stages.filter(v => v>=i).length});
  };

  return arr.sort((a, b) => {
    if (a.failRate > b.failRate) return -1;
    if (a.failRate < b.failRate) return 1;
    return a.stageNumber - b.stageNumber
  }).map(v => v.stageNumber)

}




test('solution', () => {
  expect(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])).toBe([3,4,2,1,5]);
  expect(solution(4, [4,4,4,4,4])).toBe([4,1,2,3]);
})