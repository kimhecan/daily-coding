function solution(departList, budget) {
  departList.sort();
  
  let sum = 0;
  for(let i=0; i<departList.length; i++) {
    sum += departList[i];
    console.log(sum, 'sum', i, 'i');
    if (sum > budget) return i
    if (sum == budget) return i+1
  }
}

console.log(solution([1,3,2,5,4], 9));
console.log(solution([2,2,3,3], 10));


console.log([1,1, 3,3, 2,2].sort());
