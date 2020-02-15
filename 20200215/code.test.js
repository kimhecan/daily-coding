// a - z: 97 ~ 122
// A - Z: 65 ~ 90

function solution(s, n) {

  let lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
  let upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
  let arr = s.split('');

  for(let i=0; i < arr.length; i++) {

    if (lower.includes(arr[i])) {
      let num1 = lower.indexOf(arr[i]) + n;
      if (num1 >= 26) num1 -= 26;
      arr[i] = lower[num1]
    }
    if (upper.includes(arr[i])) {
      let num2 = upper.indexOf(arr[i]) + n;
      if (num2 >= 26) num2 -= 26;
      arr[i] = upper[num2]
    } 
  }
  return arr.join('');
}


test('solution', () => {
  expect(solution('a', 1)).toBe('b');
})

test('solution', () => {
  expect(solution('ab ', 1)).toBe('bc ');
})

test('solution', () => {
  expect(solution('zZ', 1)).toBe('aA')
})

test('solution', () => {
  expect(solution('Y', 2)).toBe('A')
})
