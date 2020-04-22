function solution(money) {
  chagneMoney = 1000 - money;
  arr = [500, 100, 50, 10, 5, 1];
  count = 0;

  arr.forEach(v => {
    let val = parseInt(chagneMoney / v, 10);
    if (val > 0) {
      count += val;
      chagneMoney -= v * val;
    }
  });
  return count;
}

console.log(solution(380));
