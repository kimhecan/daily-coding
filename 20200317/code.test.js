function solution(dartResult) {
  let arrAll = dartResult.match(/\d+\w[\*\#]?/g);
  let arrDigit = dartResult.match(/\d+/g).map(v => parseInt(v));
  
  arrAll.map((v, i) => {
    v.match(/\w/g)[v.match(/\w/g).length-1] == 'D' ? arrDigit[i] = arrDigit[i] ** 2 : v.match(/\w/g)[v.match(/\w/g).length-1] == 'T' ? arrDigit[i] = arrDigit[i] ** 3 : arrDigit[i] = arrDigit[i] ** 1;
    if(v.match(/\*/g) !== null) i == 0 ? arrDigit[i] *= 2 : [i-1,i].forEach(j => arrDigit[j] *= 2);
    if(v.match(/\#/g) !== null)  arrDigit[i] = -arrDigit[i];
  })
  return arrDigit.reduce((cur, acc) => acc + cur,0);
}


test('solution', () => {
  expect(solution("1S2D*3T")).toBe(37)
  expect(solution("1D2S#10S")).toBe(9)
  expect(solution("1D2S0T")).toBe(3)
  expect(solution("1S*2T*3S")).toBe(23)
  expect(solution("1D#2S*3S")).toBe(5)
  expect(solution("1T2D3D#")).toBe(-4)
  expect(solution("1D2S3T*")).toBe(59)
  expect(solution("10D1S1T*")).toBe(104)
})