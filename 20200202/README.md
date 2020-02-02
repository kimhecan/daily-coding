### 1. 이해

문자열이 주어졌을 떄 대소문자 구분없이 p와 y의 갯수가 같으면
true를 리턴하고 아니면 false를 리턴한다. 

### 2. 계획

일단 toUpperCase() 또는 toLowerCase()를 써서 대문자든 소문자든 통일을 시킨다.
문자열에서 split함수로 배열로 바꾸고 filter로 p 또는 y만 남긴 배열의 길이를 비교한다.


### 3. 실행


### 4. 반성

문자열에서 조건찾는건 정규표현식이 최곤데...ㅎㅅㅎ

```javascript

function numPY(s) {
  return s.match(/p/ig).length == s.match(/y/ig).length;
}

```
```python
    s.lower().count('p') == s.lower().count('y')
```
python에서는 match는 객체를 리턴하기 때문에 findall을 대신 쓴다.
문자열에서 count라는 함수가 있을줄이야 역시 파이썬


### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
