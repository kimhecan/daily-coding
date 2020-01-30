### 1. 이해
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

조건에 맞는 문자열을 판별하는 문제이다.

### 2. 계획

이전에 조건에 맞는 문자열에서 for문이나 if문을 쓰면 굉장히 좀 코드가
더럽게 느꼇졌었고 그 때 유용한 정규표현식을 사용하면 깔끔한 코드가 된다.

### 3. 실행


### 4. 반성

JS 정규표현식 메소드중에 test 를 썼으면 한줄 더 줄였을 것이다..

```javascript
let result = s.match(regEx);
let answer = result == null ? false : true
return answer;

대신


return regex.test(s);
```


### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
