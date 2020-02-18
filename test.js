function solution(arr) {
  return arr.filter(v => v > Math.min.apply(null, arr))
}


let a = 10;
a /= 2;
console.log(a);

