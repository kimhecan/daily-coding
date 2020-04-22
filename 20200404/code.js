function solution(arr) {
  arr.sort((a, b) => a - b);
  let time = 0;
  return arr.reduce((acc, cur) => {
    time += cur;
    return acc += time
  }, 0)
}

console.log(solution([3, 1, 4, 3, 2]));
