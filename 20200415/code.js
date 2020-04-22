function solution(arr) {
  arr.sort((a, b) => a[1] - b[1]);
  min = 0, count = 0;
  for(let i=0; i <arr.length; i++) {
    if (arr[i][0] >= min) {
      min = arr[i][1];
      count++;
    };
  };
  return count
}

console.log(solution([[1,4], [3,5], [0,6], [5,7], [3,8], [5,9], [6,10], [8,11], [8,12], [2,13], [12,14]]));
