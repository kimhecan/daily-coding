function solution(n, m, k) {
  team = 0
  while(n >= 2 && m >= 1 && n + m >= k + 3) {
    n -= 2;
    m -= 1;
    team += 1;
  }
  return team;
}