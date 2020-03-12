function solution(n, arr1, arr2) {
  let deArray1 = arr1.map(v => parseInt(v.toString(2),10));
  let deArray2 = arr2.map(v => parseInt(v.toString(2),10));

  let sumArray = deArray1.map((v, i) => String(v + deArray2[i]).replace(/2|1|0/g, a=> +a ?  '#' : ' '));
  let answer = sumArray.map(v => ' '.repeat(n - v.length) + v);  
  
  return answer
}


test('solution', () => {
  expect(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])).toStrictEqual(["######", "###  #", "##  ##", " #### ", " #####", "### # "])
  expect(solution(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28])).toStrictEqual(["#####","# # #", "### #", "#  ##", "#####"])
})
