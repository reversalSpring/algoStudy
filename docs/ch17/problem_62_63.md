### 62 유요한 애너그램
> t가 s의 애너그램인지 판별하라

#### 입력
> s = "anagram", t = "nagaram"

#### 출력
> true

#### 입력
> s = "rat", t = "car"

#### 출력
> false

### 풀 이
```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

### 63 색 정렬
> 빨간색을 0, 흰색을 1, 파란색을 2라 할 때 순서대로 인접하는 제자리 정렬을 수행하라

#### 입력
> [2,0,2,1,1,0]

#### 출력
> [0,0,1,1,2,2]

### 풀 이
```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)
        
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1     
```
