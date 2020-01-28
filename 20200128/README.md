### 1. 이해

연속되게 같은 숫자가 나오면 하나 남기고 제거하는 문제다.

### 2. 계획

당장 생각나는건 반복문으로 앞의 숫자와 같은 경우 제거하는 방법이다.

### 3. 실행



### 4. 반성

1. filter 함수를 알았지만 쓰지 못했다

```javascript
arr.filter((val,index) => val != arr[index+1]);
```



2. Jest의 toBe와 toStrictEqual의 차이를 알게 되었다.

**toBe**
Use .toBe to compare primitive values or to check referential identity of object instances.
Don't use .toBe with floating-point numbers. try .toBeCloseTo instead.
Although the .toBe matcher checks referential identity, it reports a deep comparison of values if the assertion fails. 


**toStrictEqual**
Use .toStrictEqual to test that objects have the same types as well as structure.
