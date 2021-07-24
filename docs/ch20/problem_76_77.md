## 19. 슬라이딩 윈도우

### 76. 부분 문자열이 포함된 최소 윈도우

Https://leetcode.com/problems/minimum-window-substring

문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라

>입력
>
>> S = "ADOBECODEBANC", T = "ABC"
>
>출력
>
>> "BANC"

## 내 풀이

### 풀이 1) 모든 경우의 수 찾기 --> 당연히 실피

### 풀이 2) 투 포인터 (다른 분들 코드 참고)

## 책 풀이

### 풀이 1) 브루트 포스

#### 풀이 : 입력된 t 의 길이 보다 큰 순서대로 검색

![IMG_293C2C284F3E-1](https://user-images.githubusercontent.com/30167661/118394539-366b4180-b680-11eb-80fc-b3efca40eb54.jpeg)

#### 소스 코드 :

```python
def minWindow(self, s: str, t: str) -> str:
  def contains(s_substr_lst: List, t_lst: List):
    for t_elem in t_lst:
      if t_elem in s_substr_lst:
        s_substr_lst.remove(t_elem)
      else:
        return False
    return True
  
  if not s or not t:
    return ''
  
  window_size = len(t)
  
  for size in range(window_size, len(s) + 1):
    for left in range(len(s) - size + 1):
      s_substr = s[left:left + size]
      if contains(list(s_substr), list(t)):
        return s_substr
  return ''
```

#### 결론 : O(n^2) 시간초과 실패

### 풀이 2) 투 포인터, 슬라이딩

풀이 : 필요한 모든 문자를 찾을 때까지 오른쪽 포인터를 이동 하고 왼쪽 포인터를 오른쪽으로 이동

![IMG_FC55019B4BF1-1](https://user-images.githubusercontent.com/30167661/118394544-4125d680-b680-11eb-8fb5-04721fd7be30.jpeg)

#### 소스 코드 :

```python
def minWindow(self, s: str, t:str) -> str:
  
  # need -> 필요한 문자 각각의 개수 / missing 필요한 문자 전체 개수
  need = collections.Counter(t)
  missing = len(t)
  left = start = end = 0
  
  # 오른쪽 포인터 이동 (1 부터 시작)
  for right, char in enumerate(s, 1):
    missing -= need[char] > 0
    need[char] -= 1
    
    # 필요 문자가 0이면 왼쪽 포인터 이동 판단
    if missing == 0:
      # 왼쪽 포인터가 불필요한 문자를 가리키고 있다면 음수일 것
      while left < right and need[s[left]] < 0:
        need[s[left]] += 1
        left += 1
        
      if not end or right - left <= end - start:
        start, end = left, right
        need[s[left]] += 1
        missing += 1
        left += 1
        
  return s[start:end]
  
```

#### 다른 분들 코드를 참고한 소스 코드 :

```python
def minWindow(self, s: str, t: str) -> str:
        
        dict_t = {}
        
        # t에 주어진 문자열을 딕셔너리 자료형으로 갯수를 세어 저장
        for i in range(len(t)):
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
        
        start, end = 0, 0
        min_start = 0
        min_len = len(s) + 1
        char_to_find = len(t)

        while end < len(s):
            # 찾을 단어가 모두 없어 질때 까지 오른쪽으로 포인터 이동
            if s[end] in dict_t:
                if dict_t[s[end]] > 0:
                    char_to_find -= 1
                dict_t[s[end]] -= 1

            # 길이가 가장 작은 값이면 최소값을 업데이트 하고 왼쪽 포인터를 오른쪽로 이동
            while char_to_find == 0:
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_start = start

                if s[start] in dict_t:
                    dict_t[s[start]] += 1
                    if dict_t[s[start]] > 0:
                        char_to_find += 1

                start += 1

            end += 1

        return '' if min_len == len(s) + 1 else s[min_start : min_start + min_len]
  
```

#### 결과 :

책 풀이 -> 104ms / 14.7MB

참고 풀이 -> 88ms / 14.8MB

### 풀이 2) Counter AND로 편리한? 연산

풀이 : missing == 0 대신 Counter()의 AND 연산

소스 코드 :

```python
def minWindow(self, s: str, t:str) -> str:
        t_count = collections.Counter(t)
        current_count = collections.Counter()

        start = float('-inf')
        end = float('inf')

        left = 0
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            current_count[char] += 1

            # AND 연산 결과로 왼쪽 포인터 이동 판단
            while current_count & t_count == t_count:
                if right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1

        return s[start:end] if end - start <= len(s) else ''
```

#### 결과 : 1756ms / 14.8MB

### 77. 가장 긴 반복 문자 대체

Https://leetcode.com/problems/longest-repeating-character-replacement/

대문자로 구성된 문자열 s가 주어졌을 때 k 번 만큼의 변경으로 만들 수 있는, 연속으로 반복된 문자열의 가장 긴 길이를 출력하라.

>입력
>
>> S = "AAABBC", K = 2
>
>출력
>
>> 5

### 풀이 1) 투 포인터, 슬라이딩 윈도우, Counter를 모두 이용

오른쪽 포인터에서 왼쪽 포인터 위치를 뺀 다음, 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값

--> max(right) - min(left) - max_char_n == k

소스 코드 :

```python
def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]
            
            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
                
        return right - left
```

#### 결과 : 208ms / 14.3MB
