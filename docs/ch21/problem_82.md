## 21. 그리디 알고리즘

### 82. 쿠키 부여

Https://leetcode.com/problems/assign-cookies

아이들에게 1개씩 쿠키를 나눠줘야 한다. 
각 아이가 child_i마다 그리드 팩터g를 갖고 있으며, 
이는 아이가 만족하는 최소 쿠키의 크기를 말한다. 
각 쿠키 cookie_j는 크기g를 갖고 있으며 s >= g 이어야 아이가 만족하며 쿠키를 받는다.
최대 몇 명의 아이들에게 쿠키를 줄 수 있는지 출력하라

>입력
>
>> s = [1,2,3], g = [1,1]
>
>출력
>
>> 1

## 내 풀이

### 정렬 후 만족하는 수이면 꺼내기

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt = 0
        
        g.sort()
        s.sort()
        
        for i in range(len(s)):
            if g and g[0] <= s[i]:
                g.pop(0)
                cnt += 1
                
        return cnt
```

#### 결과 : 176ms / 16MB

## 책 풀이

### 풀이 1) 그리디 알고리즘

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i = cookie_j = 0
        
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
                
        return child_i
```

#### 결과 : 164ms / 15.9MB

### 풀이 2) 이진 검색

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
        return result
```

#### 결과 : 176ms / 16.2MB