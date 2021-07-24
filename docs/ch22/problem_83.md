## 21. 분할 정복

### 83. 과반수 엘리먼트

Https://leetcode.com/problems/majority-element/

과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라.

>입력
>
>> [3,2,3]
>
>출력
>
>> 3
>입력
>
>> [2,2,1,1,1,2,2]
>
>출력
>
>> 2

## 내 풀이

### Counter 함수 사용

```python
def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
```

#### 결과 : 156ms / 15.5MB

## 책 풀이

### 풀이 1) 브루트 포스로 과반수 비교

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num
        
```

#### 결과 : Timeout

### 풀이 2) 다이나믹 프로그래밍

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            
            if counts[num] > len(nums) // 2:
                return num
```

#### 결과 : 160ms / 15.4MB

### 풀이 3) 분할 정복

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        
        return [b, a][nums.count(a) > half]
```

#### 결과 : 160ms / 15.4MB

### 풀이 4) 파이썬 다운 방식

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
```

#### 결과 : 152ms / 15.5MB
