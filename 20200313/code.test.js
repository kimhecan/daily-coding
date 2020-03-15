function solution(n, stages) {
  let percentage = []
  let unsortPercentage = []
  let preDenominator = 0;
  let stagesLength = stages.length

  // 각 스테이지의 실패율 구하기
  for(let i=1; i<=n; i++) {
    let afterDenominator = 0;
    stages.forEach(v => v == i ? afterDenominator++ : null );
    stagesLength -= preDenominator;
    percentage[i-1] = afterDenominator / stagesLength;
    unsortPercentage[i-1] = afterDenominator / stagesLength;
    preDenominator = afterDenominator;
  }
  percentage.sort((a, b) => b-a);

  let answer = [];
  // 실패율에 따른 정렬과 인덱스 저장
  percentage.forEach((v, i) => {
    answer[i] = unsortPercentage.indexOf(percentage[i])+1;
    unsortPercentage.splice(unsortPercentage.indexOf(percentage[i]),1,4);
  })
  return answer;
}





test('solution', () => {
  expect(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])).toBe([3,4,2,1,5]);
  expect(solution(4, [4,4,4,4,4])).toBe([4,1,2,3]);
})