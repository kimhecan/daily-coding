/* 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요. */

function solution(participant, completion) {
  const participantObj = participant.reduce((acc, crr) => {
  acc[crr] ? acc[crr] += 1 : acc[crr] = 1 
  return acc;
}, {})

  completion.forEach((name,i) => {
    participantObj[name] -= 1;
  })
  
  for(let i in participantObj) {
      if (participantObj[i] === 1) {
          return i
      } 
  }
}



test('solution', () => {
  expect(solution(["leo", "kiki", "eden"],["eden", "kiki"])).toBe("leo");
  expect(solution(["marina", "josipa", "nikola", "vinko", "filipa"]	,["josipa", "filipa", "marina", "nikola"])).toBe("vinko");
  expect(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])).toBe("mislav");
});