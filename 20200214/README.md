### 1. 이해

리스트와 숫자(인덱스)가 주어졌고 인덱스의 알파벳에 따라 정렬된 리스트를 리턴한다.

### 2. 계획

주어진 인덱스에 알파벳을 각 문자 앞에 붙여주고 정렬한다. 그리고 붙였던 맨 앞 알파벳을 제거한다

### 3. 실행



### 4. 반성


파이썬에서 sorted에 두번쨰 인자로 정렬기준을 잡을 수 있다는 것을 알게됨

```python
sorted(strings, key=lambda x: x[n])

sorted("This is a test string from Andrew".split(), key=str.lower)

sorted(student_tuples, key=lambda student: student[2])
```


### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
