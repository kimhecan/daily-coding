function solution(n) {
  
  let arr = new Array(n+1);
  arr[0] = arr[1] = false;
  for(let i=2; i <=n; i++) arr[i] = true;
  
  for(let i=2; i < Math.sqrt(n); i++) {
    let mult = 2;
    if (arr) {
      for(let j = i * mult; j <= n; j = i * mult) {
        arr[j] = false;
        mult++;
      }
    }
  }

  let answer = arr.map((v, i) => {
    if(v == true) return i;
    else return v
  }).filter(v => v !== false)

  return answer.length
}



test('solution', () => {
  expect(solution(10)).toBe(4)
});

test('solution', () => {
  expect(solution(5)).toBe(3)
});