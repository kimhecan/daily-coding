function solution(participant, completion) {
  let parObj = participant.reduce((acc, cur) => {
    acc[cur] ? acc[cur] += 1 : acc[cur] = 1;
    return acc
  }, {});
  completion.forEach((v, i) => {
    parObj[v] -= 1;
  })
  for (let i in parObj) {
    if (parObj[i] == 1) {
      console.log(i);
    }
  }
}

solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav'])