function solution(arr) {
  arr.sort((a, b) => b - a);
  max = 0;
  for (let i=0; i<arr.length; i++) {
    if(max < arr[i] * (i+1)){
      max = arr[i] * (i+1)
    } else {
      return max
    }
  }
  return max
}

console.log(solution([10,20,30]));
console.log(solution([10,15]));