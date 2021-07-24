## 72. 두 정수의 합

- https://leetcode.com/problems/sum-of-two-integers/

>**371. Sum of Two Integers** (Medium)
>
>Given two integers `a` and `b`, return *the sum of the two integers without using the operators* `+` *and* `-`.
>
> 
>
>**Example 1:**
>
> ```
>Input: a = 1, b = 2
>Output: 3
>```
>
>**Example 2:**
> 
>```
>Input: a = 2, b = 3
>Output: 5
>```
>
> 
>
>**Constraints:**
>
>- `-1000 <= a, b <= 1000`

  

### 1) 전가산기 구현

- 전가산기 진리표(Truth Table)와 회로도

  - AND 게이트 2개, XOR 게이트 2개, OR 게이트 1개
    - Q1 = A & B
    - Q2 = A ^ B
    - Q3 = Q2 & carry
    - sum = carry ^ Q2
    - carry = Q1 | Q3

  ![image](https://user-images.githubusercontent.com/19264527/117527542-d46b6600-b007-11eb-9804-df113d8ec9d3.png)

- ` a `정수를 `a_bin` 이진수로 변경하는 전처리 로직

  ```python
  MASK = 0xFFFFFFFF
  a_bin = bin(a & MASK)[2:].zfill(32)
  ```

  - `bin()` - 10진수를 2진수로 변환

    ```python
    >>> bin(10)
    '0b1010's
    ```

  - 필요없는 파이썬 이진수 식별자 '0b' 제거

    ```python
    bin(a)[2:1]
    ```

  - 음수처리를 위해 2의 보수로 만들어주는 마스킹 작업 (32비트)

    - 양수인 경우 마스킹해도 동일

    ```python
    >>> bin(1 & MASK) 
    '0b1'
    >>> bin(-1 & MASK)
    '0b11111111111111111111111111111111'
    ```

  - 32비트 자릿수 맞춰주기

    ```python
    >>> '1'.zfill(32)
    '00000000000000000000000000000001'
    ```

- 전처리 한 값을 뒷부분(낮은 자릿수)부터 하나씩 전가산기를 통과하면서 결과를 채워나감

  - 32번 반복
  - 마지막 반복이 끝난 후 `carry` 값이 남아있다면 자릿수가 하나 더 올라간 것
    - 1을 추가 - 33비트가 되겠지만 마스킹 작업통해 날림

  ```python
  for i in range(32):
      A = int(a_bin[31 - i])
      B = int(b_bin[31 - i])
              
      # 전가산기 구현
      Q1 = A & B
      Q2 = A ^ B
      Q3 = Q2 & carry
      sum = carry ^ Q2
      carry = Q1 | Q3
              
      result.append(str(sum))
  if carry == 1:
      result.append('1')
      
  # 초과 자릿수 처리
  result = int(''.join(result[::-1]), 2) & MASK
  ```

- 초과 자릿수 처리

  - 낮은 값부터 채웠으므로 뒤집은 다음 십진수 정수로 바꿔준다

  ```python
  result = int(''.join(result[::-1]), 2) & MASK
  ```

  - 마스킹을 통해 자릿수를 초과했다면 그 값은 제거

  ```python
  >>> int('0b1000000000000000000000000000000001', 2) & MASK
  '1'
  ```

- 음수 처리

  - 2의 보수에서 음수는 32번째 비트, 즉 최상위 비트가 1인 경우
  - 양의 정수 최댓값은 0x7FFFFFFF이므로, 만약 32번째 비트가 1이라면 이보다 큰 값이므로 마스킹 값과 XOR 후 NOT 처리를 해서 음수로 만들어 준다.

  ```python
  INT_MAX = 0x7FFFFFFF
  
  # 음수 처리
  if result > INT_MAX:
      result = ~(result ^ MASK)
  ```

#### 전체 풀이

 ```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)
        
        result = []
        carry = 0
        sum = 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])
            
            # 전가산기 구현
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3
            
            result.append(str(sum))
        if carry == 1:
            result.append('1')
            
        # 초과 자릿수 처리
        result = int(''.join(result[::-1]), 2) & MASK
        
        # 음수 처리
        if result > INT_MAX:
            result = ~(result ^ MASK)
            
        return result
 ```

  

### 2) 좀 더 간소한 구현

- 핵심만 살리기

  - 2의 보수로 만들기 위한 MASK
  - a - carry 값을 고려하지 않는 a와 b의 합
    - XOR - 두 비트가 다르면 1, 같으면 0
    - 1+0, 0+1은 1을 반환하므로, 올림수가 발생하는 1+1을 제외하고 덧셈 가능
  - b - 자리수를 올려가며 carry값 저장
    - AND - 두 비트가 모두 1이면 1, 아니면 0
    - AND 연산을 통해 올림수가 발생해서 왼쪽의 비트를 +1 해줘야 하는 1+1 연산 결과에 << 왼쪽 시프트 연산
    - AND 연산 값이 0이라서 더 이상 올림수가 없을 때 반복 종료
  
  ```python
  a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
  ```

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        # 합, 자릿수 처리
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            
        # 음수 처리
        if a > INT_MAX:
            a = ~(a ^ MASK)
            
        return a
```



## 73. UTF-8 검증

- https://leetcode.com/problems/utf-8-validation/

>**393. UTF-8 Validation** (Medium)
>
>Given an integer array `data` representing the data, return whether it is a valid **UTF-8** encoding.
>
>A character in **UTF8** can be from **1 to 4 bytes** long, subjected to the following rules:
>
>1. For a **1-byte** character, the first bit is a `0`, followed by its Unicode code.
>2. For an **n-bytes** character, the first `n` bits are all one's, the `n + 1` bit is `0`, followed by `n - 1` bytes with the most significant `2` bits being `10`.
>
>This is how the UTF-8 encoding would work:
>
>```
>   Char. number range  |        UTF-8 octet sequence
>      (hexadecimal)    |              (binary)
>   --------------------+---------------------------------------------
>   0000 0000-0000 007F | 0xxxxxxx
>   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
>   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
>   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
>```
>
>**Note:** The input is an array of integers. Only the **least significant 8 bits** of each integer is used to store the data. This means each integer represents only 1 byte of data.
>
> 
>
>**Example 1:**
>
>```
>Input: data = [197,130,1]
>Output: true
>Explanation: data represents the octet sequence: 11000101 10000010 00000001.
>It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
>```
>
>**Example 2:**
>
>```
>Input: data = [235,140,4]
>Output: false
>Explanation: data represented the octet sequence: 11101011 10001100 00000100.
>The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
>The next byte is a continuation byte which starts with 10 and that's correct.
>But the second continuation byte does not start with 10, so it is invalid.
>```
>
> 
>
>**Constraints:**
>
>- `1 <= data.length <= 2 * 104`
>- `0 <= data[i] <= 255`

- 입력 값이 UTF-8 문자열이 맞는지 검증

   

### 1) 첫 바이트를 기준으로 한 판별

- UTF-8 바이트 순서의 이진 포맷

  ```
     Char. number range  |        UTF-8 octet sequence
        (hexadecimal)    |              (binary)
     --------------------+-----------------------------------------
     0000 0000-0000 007F | 0xxxxxxx
     0000 0080-0000 07FF | 110xxxxx 10xxxxxx
     0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
     0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
  ```

- 첫 바이트가 1110으로 시작한다면 3바이트 문자 

  - 첫 바이를 제외하고 뒤따르는 2바이트는 모두 10으로 시작해야 유효한 UTF-8 문자가 된다.
  - 예제 2의 경우 세 번째 바이트가 00으로 시작하여 정상적인 UTF-8 문자가 아니다.

- 유니코드 문자의 UTF-8 인코딩

  - 예) 문자 '한' - 유니코드 1101010101011100 
    - 16비트
    - UTF-8 인코딩으로는 3바이트로 표현 가능
    - **1110**1101 **10**010101 **10**011100

  

- `first`는 첫 바이트. 

  - 0 - 1바이트 문자
  - 110 - 2바이트 문자
  - 1110 - 3바이트 문자
  - 11110 - 4바이트 문자

  ```python
  start = 0
  while start < len(data):
      # 첫 바이트 기준 총 문자 바이트 판별
      first = data[start]
      if (first >> 3) == 0b11110 and check(3):
          start += 4
      elif (first >> 4) == 0b1110 and check(2):
          start += 3
      elif (first >> 5) == 0b110 and check(1):
          start += 2
      elif (first >> 7) == 0:
          start += 1
      else:
          return False
      return True
  ```

  

- `check()` - `size`를 파라미터로 받아 해당 사이즈만큼 바이트가 10으로 시작하는지 판별

  - 앞서 첫 바이트 기준으로 3바이트 문자라고 판별했다면, 나머지 2바이트가 모두 10으로 시작하는지 판별

  ```python
  def check(size):
      for i in range(start + 1, start + size + 1):
          if i >= len(data) or (data[i] >> 6) != 0b10:
              return False
      return True
  ```

  

####  전체 풀이

```python
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트만큼 10으로 시작 판별
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True
        
        start = 0
        while start < len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True
```

  

### 내 풀이

```python
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def isUtf8(start, end):
            if end > len(data): 
                return False
            
            while start < end :
                if (data[start] >> 6) != 0b10:
                    return False
                start += 1
            return True
        
        index = 0
        while index < len(data):
            num = data[index]
            if (num >> 7) == 0:
                index += 1
            elif (num >> 5) == 0b110 and isUtf8(index + 1, index + 2):
                index += 2
            elif (num >> 4) == 0b1110 and isUtf8(index + 1, index + 3):
                index += 3
            elif (num >> 3) == 0b11110 and isUtf8(index + 1, index + 4):
                index += 4
            else:
                return False
        return True
            
                
```