# 19장 비트 조작
## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [1비트의 개수 (Number of 1 Bits)](#1)


## <a name='1'>[#191 - 1비트의 개수 (Number of 1 Bits)](https://leetcode.com/problems/number-of-1-bits/)</a>
### 문제
![image](https://user-images.githubusercontent.com/75566147/118351778-cc2ba180-b598-11eb-8e9b-2c55e2a9cfa5.png)

### (1) 내 풀이
```python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        bin = format(n, 'b')
        return bin.count('1')
```
- Point
  - format()을 사용해서 이진수로 변환한 결과를 문자열로 받고, 거기서 1의 수를 세는 방식을 사용
  - ```python3
    num = 9
    
    bin(num)             # 0b1001
    format(num, '#b')    # 0b1001
    format(num, 'b')     # 1001
    int('0b1001', 2)     # 9
    str(0b1001)          # 9
    ```

### (2) 책 풀이 - 단순
```python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```
- Point
  - 내 풀이와 동일

### (3) 책 풀이 - 비트 연산
```python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n-1
            count += 1
        return count
```
- Point
  - n이 0이 될 때까지 1을 뺀 값과 AND 연산을 한 횟수를 리턴하면 1비트의 개수를 구할 수 있다.
  - & 연산 : 두 값이 모두 1일 때 1이 나옴
  - ![image](https://user-images.githubusercontent.com/75566147/118352721-de5c0e80-b59d-11eb-8b9b-8c4643935994.png)
  - [브라이언 커니핸의 알고리즘(Brian Kernighan’s Algorithm)](https://www.geeksforgeeks.org/count-set-bits-in-an-integer/)
    - 어떤 십진수(N)에서 1을 빼면(M), (N을 이진수로 바꾼 것을 오른쪽에서부터 봤을때 가장 처음 1인 비트부터 끝 비트까지 비트를 뒤집은 결과) == (M을 이진수로 바꾼 결과) 이다.
    - 그래서 N과 M을 & 연산을 하면 N의 가장 오른쪽 set bit(이진법에서 1을 이렇게 부름)를 0으로 바꿀 수 있다.
    - 결론적으로 N을 이진수로 변환했을 때 보이는 1의 개수는 n & (n-1) 연산을 n이 0이 될 때까지 반복적으로 실행한 횟수와 동일하다.

### (4) 성능 비교
||방식|실행 시간(ms)|
|---|---|---|
|나|단순|24|
|책|단순|24|
|책|비트 연산|24|


끝.

