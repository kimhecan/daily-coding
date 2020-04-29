function solution(n) {
  let arr = n.toString().split('')
  arr.sort((a,b) => b - a);

  if (!arr.includes('0')) return -1;
  if (n % 3 != 0) return -1;

  return parseInt((arr.join("")));
}

console.log(solution(201));
