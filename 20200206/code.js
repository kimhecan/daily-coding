function solution(answers) {
  let scores = [0, 0, 0];

  for(let i=0; i< answers.length; i++) {
    if (answers[i] == (i % 5) + 1) {
      scores[0]++
    }

    if (i % 2 == 0) {
      if (answers[i] == 2) scores[1]++ 
    } else {
      if (i % 8 == 1 || i % 8 == 3) {
        if (answers[i] == i % 8) scores[1]++
      } else if (i % 8 == 5) {
        if (answers[i] == (i % 8) - 1) scores[1]++
      } else if (i % 8 == 7) {
        if (answers[i] == (i % 8) - 2) scores[1]++
      }
    }

    if (i % 10 == 0 || i % 10 == 1) {
      answers[i] == 3 ? scores[2]++ : null; 
    }
    if (i % 10 == 2 || i % 10 == 3) {
      answers[i] == 1 ? scores[2]++ : null; 
    }
    if (i % 10 == 4 || i % 10 == 5) {
      answers[i] == 2 ? scores[2]++ : null; 
    }
    if (i % 10 == 6 || i % 10 == 7) {
      answers[i] == 4 ? scores[2]++ : null; 
    }
    if (i % 10 == 8 || i % 10 == 9) {
      answers[i] == 5 ? scores[2]++ : null; 
    }
  }
  let answer = scores[0];
  for(let i=1; i<scores.length; i++) {
    if(answer < scores[i]) answer = scores[i];
  }
  let index = [];
  scores.forEach((v, i) => {
    if (v == answer) {
      index.push(i)
    }
  })
  return index
}

console.log(solution([1,2,3,4,5]));
console.log(solution([1,3,2,4,2]));

// 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5 
// index % 2 == 0  => 2
// index % 2 == 1 => 
// 1 => index % 8 = 1
// 3 => index % 8 = 3
// 4 => (index % 8) -1 = 4
// 5 => (index % 8) = 7 
// 1 1
// 3 3
// 5 4
// 7 5
// 9 1
// 11 3
// 13 4
// 15 5
// 17 1
// 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5

//01 index % 10 = => 3
//23 index % 10 = => 1
//45 index % 10 = => 2
//67 index % 10 = => 4
//89 index % 10 = => 5