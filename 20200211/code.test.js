function solution(arr1, arr2) {
    let answer = arr1.map((v, i) => v.map((k, j) => arr1[i][j] + arr2[i][j]))

    return answer;
}

test('solution', () => {
    expect(solution([[1,2],[2,3]],[[3,4],[5,6]])).toStrictEqual([[4,6],[7,9]])
});

test('solution', () => {
    expect(solution([[1],[2]],[[3],[4]])).toStrictEqual([[4],[6]])
});