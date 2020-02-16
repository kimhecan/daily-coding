### 1. 이해

대소문자

### 2. 계획

루프돌면서 바꾸면 될듯

### 3. 실행

### 4. 반성

막상 다른 사람들이 푼것을 보니까 아직 내가 한참 부족하단것을 알게 되었다.


js에서는 정규표현식으로 간단하게 풀 수 있었고
```javascript
s.toUpperCase().replace(/(\w)(\w)/g, function(a){return a[0].toUpperCase()+a[1].toLowerCase();})
```

파이썬에서는 비슷하게 접근했지만 lambda 함수안에 enumerate반복문을 쓰지 못했다. 특히 a.lower() if ~ else a.upper() for i,a ~부분은 흑흑..

```python
" ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
```


### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
