function solution(n, arr1, arr2) {
  let deArray1 = arr1.map(v => parseInt(v.toString(2),10));
  let deArray2 = arr2.map(v => parseInt(v.toString(2),10));

  let sumArray = deArray1.map((v, i) => String(v + deArray2[i]).replace(/2|1|0/g, a=> +a ?  '#' : ' '));
  let answer = sumArray.map((v, i) => ' '.repeat(n - v.length) + v);  
  
  return answer
}

solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])