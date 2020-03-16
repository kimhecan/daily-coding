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

console.log(solution(5,[4,4,4,4,4]));
console.log(  4-0/0);
