# 6장 문자열 조작

## 1. 유효한 팰린드롬

- https://leetcode.com/problems/valid-palindrome

>**125. Valid Palindrome** (Easy)
>
>Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
>
>**Note:** For the purpose of this problem, we define empty string as valid palindrome.
>
>**Example 1:**
>
>```
>Input: "A man, a plan, a canal: Panama"
>Output: true
>```
>
>**Example 2:**
>
>```
>Input: "race a car"
>Output: false
>```

### 내 풀이

```python
# Runtime 284 ms / Memory 19.7 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []
        for c in s:
            if c.isalpha() or c.isdigit():
                str.append(c.lower())

        while len(str) > 1:
            if str.pop(0) != str.pop():
                return False

        return True
```

  

### 1) 리스트로 변환

1. 영문자, 숫자만 `strs` 리스트에 추가
2. `strs` 의 맨 앞과 뒤에서 하나씩 꺼내어 같은지 비교

```python
# Runtime 280 ms / Memory 19.6 MB
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
```

- [`str.isalnum()`](https://docs.python.org/3/library/stdtypes.html#str.isalnum) - 영문자, 숫자 여부를 판별하는 함수
- [`str.lower()`](https://docs.python.org/3/library/stdtypes.html#str.lower)- 소문자로 변환된 문자열의 복사본 리턴 
- [`list.pop([i])`](https://docs.python.org/3/tutorial/datastructures.html) - 리스트에서 주어진 위치에 있는 항목을 삭제하고, 그 항목을 리턴 (인덱스  지정하지 않으면 마지막 항목을 삭제하고 리턴)



### 2) 데크 자료형을 이용한 최적화

- 데크(Deque)를 명시적으로 선언하여 속도 향상 (1번 풀이 대비 5배)
  - `list.pop(0)` - <img src="https://latex.codecogs.com/gif.latex?O(n)" /> (리스트 구현은 <img src="https://latex.codecogs.com/gif.latex?O(n^2)" />)
  - `duque.popleft()` -  <img src="https://latex.codecogs.com/gif.latex?O(1)" />  (리스트 구현은 <img src="https://latex.codecogs.com/gif.latex?O(n)" />)

```python
# Runtime 48 ms / Memory 19.5 MB
def isPalindrome(self, s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
```

- [`deque.popleft()`](https://docs.python.org/3/library/collections.html#collections.deque.popleft) - deque의 왼쪽 원소 제거하고 값 리턴

  

### 3) 슬라이싱 사용

1. 정규식으로 불필요한 문자 필터링
2. 문자열 슬라이싱 `[::-1]`을 이용하여 뒤집어 비교

```python
# Runtime 36 ms / Memory 15.6 MB
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱
```

- [`re.sub(pattern, repl, string, count=0, flags=0)`](https://docs.python.org/ko/3/library/re.html#re.sub)

  :  패턴에 일치되는 문자열을 다른 문자열로 바꿔줌. 

  - [^a-z0-9] : a-z, 0-9에 매칭되지 않는 문자

​    

#### 문자열 슬라이싱

- 문자열을 조작할 때 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리

```python
# 0 1 2 3 4
# 안녕하세요
# -5 -4 -3 -2 -1

s = '안녕하세요'
s[1:4]	# 녕하세
s[1:-2]	# 녕하
s[1:]		# 녕하세요
s[:]		# 안녕하세요 (사본 리턴, 참조가 아닌 값 리턴)
s[1:100]# 녕하세요
s[-1]		# 요
s[-4]		# 녕	
s[:-3]	# 안녕
s[-3:]	# 하세요
s[::1]	# 안녕하세요
s[::-1]	# 요세하녕안 (뒤집는다)
s[::2]	# 안하요
```



### 4) C 구현

- C와 같은 컴파일 언어는 파이썬과 같은 인터프리터 언어에 비해 더 좋은 성능을 낸다.
- 문자열을 저장하는 char 포인터에 대한 직접 조작

```c
# Runtime 0 ms / Memory 6.5 MB
bool isPalindrome(char * s){
    int bias_left = 0;
    int bias_right = 1;
    
    int str_len = strlen(s);
    for(int i = 0; i < str_len; i++) {
        // 스킵 포인터 처리
        while(!isalnum(s[i + bias_left])) {
            bias_left++;
            if(i + bias_left == str_len)
                return true;
        }
        while(!isalnum(s[str_len - i - bias_right])) {
            bias_right++;
        }
        if(i + bias_left >= str_len - i - bias_right)
            break;
        
        // 팰린드롬 비교
        if(tolower(s[i + bias_left]) != tolower(s[str_len - i - bias_right]))
            return false;
    }
    return true;
}
```

  

### 풀이 비교

| 풀이 | 방식                        | 실행시간 |
| ---- | --------------------------- | -------- |
| 1    | 리스트로 변환               | 304 ms   |
| 2    | 데크 자료형을 이용한 최적화 | 64 ms    |
| 3    | 슬라이싱 사용               | 36 ms    |
| 4    | C 구현                      | 4 ms     |

  

## 2. 문자열 뒤집기

- https://leetcode.com/problems/reverse-string

>**344. Reverse String** (Easy)
>
>Write a function that reverses a string. The input string is given as an array of characters `char[]`.
>
>Do not allocate extra space for another array, you must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.
>
>You may assume all the characters consist of [printable ascii characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters).
>
>**Example 1:**
>
>```
>Input: ["h","e","l","l","o"]
>Output: ["o","l","l","e","h"]
>```
>
>**Example 2:**
>
>```
>Input: ["H","a","n","n","a","h"]
>Output: ["h","a","n","n","a","H"]
>```

### 내 풀이

```python
# Runtime 1064 ms / Memory 18.5 MB
class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for i in range(length):
            c = s.pop()
            s.insert(i, c)
```

  

### 1) 투 포인터를 이용한 스왑

-  2개의 포인터를 이용해 범위를 좁혀가며 문자열 내부에서 스왑하는 형태

```python
# Runtime 192 ms / Memory 18.7 MB
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```



### 2) 파이썬 다운 방식

- 파이썬의 기본기능을 이용하여 한 줄로 풀이 (파이썬 다운 방식)

```python
# Runtime 192 ms / Memory 18.7 MB
def reverseString(self, s: List[str]) -> None:
    s.reverse()
```

- 공간복자도를 <img src="https://latex.codecogs.com/gif.latex?O(1)" /> 로 제한하므로 변수 할당을 처리하는 데 제약이 있다.

```python
# Runtime 192 ms / Memory 18.6 MB
def reverseString(self, s: List[str]) -> None:
    # s = s[::-1] - 오류 발생
    s[:] = s[::-1] # 트릭 이용
```

####  ++

https://stackoverflow.com/questions/32448414/what-does-colon-at-assignment-for-list-do-in-python

This syntax is a slice assignment. A slice of `[:]` means the entire list. The difference between `nums[:] =` and `nums =` is that the latter doesn't replace elements in the original list. This is observable when there are two references to the list

```py
>>> original = [1, 2, 3]
>>> other = original
>>> original[:] = [0, 0] # changes the contents of the list that both
                         # original and other refer to 
>>> other # see below, now you can see the change through other
[0, 0]
```

To see the difference just remove the `[:]` from the assignment above.

```py
>>> original = [1, 2, 3]
>>> other = original
>>> original = [0, 0] # original now refers to a different list than other
>>> other # other remains the same
[1, 2, 3]
```

  

### 풀이 비교

| 풀이 | 방식                    | 실행시간 |
| ---- | ----------------------- | -------- |
| 1    | 투 포인터를 이용한 스왑 | 216 ms   |
| 2    | 파이썬 다운 방식        | 208 ms   |

  

## 3. 로그파일 재정렬

- https://leetcode.com/problems/reorder-data-in-log-files

>**937. Reorder Data in Log Files (Easy)**
>
>You have an array of `logs`. Each log is a space delimited string of words.
>
>For each log, the first word in each log is an alphanumeric *identifier*. Then, either:
>
>- Each word after the identifier will consist only of lowercase letters, or;
>- Each word after the identifier will consist only of digits.
>
>We will call these two varieties of logs *letter-logs* and *digit-logs*. It is guaranteed that each log has at least one word after its identifier.
>
>Reorder the logs so that all of the letter-logs come before any digit-log. The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties. The digit-logs should be put in their original order.
>
>Return the final order of the logs.
>
>**Example 1:**
>
>```
>Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
>Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
>```

- 로그의 가장 앞 부분은 식별자다
- 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
- 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
- 숫자로그는 입력 순서대로 한다.

  

### 내 풀이

```python
# Runtime 36 ms / Memory 14.3 MB
class Solution:
    def key_fun(self, e):
        return e.split()[1:], e.split()[0]
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        alpha = []
        for str in logs:
            arr = str.split()
            if arr[1].isdigit():
                digit.append(str)
            else:
                alpha.append(str)
            
        alpha.sort(key=self.key_fun)
        return alpha + digit 
```

  

### 1) 람다와 연산자를 이용

- 요구조건을 얼마나 깔끔하게 처리할 수 있는지 묻는 문제

1. 문자와 숫자를 구분하고 숫자는 나중에 그대로 이어 붙인다.
2. 문자 로그들을 정렬

```python
# Runtime 40 ms / Memory 14.2 MB
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
```

  

#### 람다 표현식

- 식별자 없이 실행 가능한 함수
- 함수의 선언 없이도 하나의 식으로 함수를 표현
- 리스트 컴프리헨션(List Comprehension)이 훨씬 더 간결하고 가독성이 좋으므로 주로 사용할 예정

```python
def func(x):
  return x.split()[1], x.split()[0]

s.sort(key=func)
  
s.sort(key=lambda x: (x.split()[1], x.split()[0]))
```

