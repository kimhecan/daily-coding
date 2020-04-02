function solution(arr, k) {
  count = arr.reverse().reduce((acc, cur) => {
    if (parseInt(k / cur) > 0) {
      acc += parseInt(k / cur);
      k %= cur;
    }
    return acc 
  }, 0)

  return count;

}


console.log(solution([1,5,10,50,100,500,1000,5000], 4790))