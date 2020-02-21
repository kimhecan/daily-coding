### 1. 이해

별표찍기

### 2. 계획

반복문

### 3. 실행


### 4. 반성

반성이라기보다 새로운 것을 알게 되었다. 자바스크립트에서 커멘트라인입력을 받는법이다.

```javascript
process.stdin.resume();
process.stdin.setEncoding('utf8');
//event 등록하기
process.stdin.on('data', function(chunk) {
    // 출력하기
    process.stdout.write('data' + chunk);
});
//종룍하기
process.stdin.on('end', function() {
    process.stdout.write('end');
});
```


### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
