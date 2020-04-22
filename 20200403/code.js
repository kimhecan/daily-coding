function solution(people, limit) {
  people.sort((a, b) => a - b);
  console.log(people);
  let light = 0;
  let heavy = people.length - 1;
  let count = 0;
  
  while (light <= heavy) {
    count += 1;
    if (people[light] + people[heavy] <= limit) {
      light += 1;
    }
    heavy -= 1;
  }
  return count;
}


console.log(solution([70,50,80,50],100));
console.log(solution([40,50,60,70,80,90],100));
