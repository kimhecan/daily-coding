function solution(string) {
  sum = 0;
  arr = string.split("-");

  arr[0].split("+").forEach(v => sum += parseInt(v, 10));

  arr.slice(1).forEach(v => {
    v.split("+").forEach(k => sum -= parseInt(k, 10))
  });

  return sum;
}

console.log(solution("55-50+40"));
console.log(solution("55-50+40-10+20+20"));
