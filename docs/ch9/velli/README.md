# 9-21 316. Remove Duplicate Letters
초기 접근법은 1번만 나온 문자와 N번 나온 문자를 분류해서 정렬 후 합치는 방식을 택했지만 문제를 잘 못 이해한거였음
N번 나온 문자는 1번만 나오도록 지우되 그 문자가 나올 위치는 사전순 정렬에 위배되면 안됨

### testcase1
ecbeacedcebc ==> acdeb

- ['e']
- ['c']
- ['b']
- ['b', 'e']
- ['a']
- ['a', 'c']
- ['a', 'c', 'e']
- ['a', 'c', 'd']
- ['a', 'c', 'd', 'e']
- ['a', 'c', 'd', 'e', 'b']


### testcase2
ecbeacedcebce ==> acdbe

- ['e']
- ['c']
- ['b']
- ['b', 'e']
- ['a']
- ['a', 'c']
- ['a', 'c', 'e']
- ['a', 'c', 'd']
- ['a', 'c', 'd', 'e']
- ['a', 'c', 'd', 'b']
- ['a', 'c', 'd', 'b', 'e']

1. []
2. ['e']
3. ['c']
4. ['b']
5. ['b', 'e']
6. ['a']
7. ['a', 'c']
8. ['a', 'c', 'e']
9. ['a', 'c', 'd']
10. ['a', 'c', 'd']
11. ['a', 'c', 'd', 'e']
12. ['a', 'c', 'd', 'b']
13. ['a', 'c', 'd', 'b']


```python

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        origin_counter = collections.Counter(s)
        stack = []
        
        check_list = set()
        
        for char in s:
            origin_counter[char] -= 1
            if char in check_list:
                continue
            
            # (stack is not empty) && (사전순 규칙을 어겼을 때) && (N번 나온 문자일 때)
            while stack and stack[-1] > char and origin_counter[stack[-1]] > 0:
                # 스택에서 제거
                check_list.remove(stack.pop())
                
            
            stack.append(char)
            # 처음 나온 문자기이 때문에 추가
            check_list.add(char)
            
        
        
        
        return ''.join(stack)
```



# 9-22 739. Daily Temperature
## 나의 풀이
```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for i in range(len(T))]
        stack = []

        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1] - i
            else:
                result[i] = 0
                
            stack.append(i)
        
        return result
```



## 교재 풀이
```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T) # list comprehension보다 직관적인 듯56
        stack = []
        for i, cur in enumerate(T): # enumerate를 사용할 생각을 못함.
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer
```


## 단순 풀이
```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for i in range(len(T))]
        for i in range(len(T)):
            count = 0
            for j in range(i+1, len(T)):
                if T[i] < T[j]:
                    count += 1
                    result[i] = count
                    break
                else:
                    count +=1
        return result
```
해당 기온에 대해 그 다음 날짜의 기온들을 하나씩 탐색하면서 count를 세는 단순한 방식.
예전 java 풀이 시에는 이 알고리즘도 느리긴 했지만 `Accepted`를 받았지만 파이썬은 아예 실패했음.


## 풀이별 비교
| Status              | Runtime | Memory  | Language |
|---------------------|---------|---------|----------|
| Time Limit Exceeded |         |         | python3  |
| Accepted            | 508 ms  | 18.6 MB | python3  |
| Accepted            | 59 ms   | 43.9 MB | java     |
| Accepted            | 221 ms  | 42.5 MB | java     |