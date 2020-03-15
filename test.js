function solution(n, stages) {
  let percentage = []
  let unsortPercentage = []
  let preDenominator = 0;
  let stagesLength = stages.length

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
  percentage.forEach((v, i) => {
    answer[i] = unsortPercentage.indexOf(percentage[i])+1;
    unsortPercentage.splice(unsortPercentage.indexOf(percentage[i]),1,4);
  })
  return answer;
}

console.log(solution(5,[2,1,2,6,2,4,3,3]));
console.log(solution(4,[4,4,4,4,4]));
console.log(solution(1,[1,1,1,1,1,1]));
console.log(solution(2,[1,3]));
console.log(solution(10,[1,1,1,2,2,3,3,3,7,9]));