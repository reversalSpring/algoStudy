# 6장 문자열 조작

## 4. 그룹 애너그램

- https://leetcode.com/problems/group-anagrams/

**819. Most Common Word**
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

**Example 1:**

```
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
```

### 풀이 및 코드

1. 문장을 소문자로 변경
2. import re <-- re.sub에 정규식을 통해 문자를 추출하고 split() 함수로 공백단위 List로 변환
3. not in 으로 인해 banned(금지) 단어 제회
4. output.key()를 추춘하고 lambda로 output[k] 값 추출하여 max 값 추출

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        output = defaultdict(list)

        # 리스트 컴프리헨션으로 축약 가능 
        # word = [word for word in re.sub(r'[^/w]', ' ', paragraph).lower().split() if word not in banned]
        paragraph = paragraph.lower()
        paragraph_to_word = re.sub('[^a-z]',' ',paragraph).split()
        
        for i in paragraph_to_word:
            if i not in banned:
                output[i] += 1

        #count로 가능 
        # ex) counts = collections.Counter(output)
        #     return counts.most_common(1)[0][0]
        return max(output.keys(), key=(lambda k: output[k]))
```

## 5. 그룹 애너그램

- https://leetcode.com/problems/group-anagrams/

**49. Group Anagrams**
문자열 배열을 받아 애너그램 단위로 그룹핑하라

**Example 1**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**
```
Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
```

### 풀이 및 코드

1. 값이 없을시 디폴트값을 넣기 위해 defaultdict로 촉기화
2. sorted로 단어를 정렬한 후 join으로 합친 후 하나씩 append
3. list로 한번더 변형서 리턴해야 하는 줄 알았으나 output.values()를 하면 자동으로 List변환됨

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for i in strs:
            output[''.join(sorted(i))].append(i)
        
        return list(output.values())
```

## 6. 가장 긴 팰린드롬 부분 문자열

- https://leetcode.com/problems/longest-palindromic-substring/

**5. Longest Palindrome Substring**
가장 긴 팰린드롬 부분 문자열을 출력하라

**Example 1:**
```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

**Example 3:**
```
Input: s = "a"
Output: "a"
```

**Example 4:**
```
Input: s = "ac"
Output: "a"
```

### 풀이 및 코드

1. expand를 단순히 문자열을 넘어가지 않고 왼쪽 오른쪽이 같으면 범위를 늘리는 용도
2. 만약 길이가 2 이하거나 문자열을 뒤집었을 때 똑같다면 단어 그대로 리턴
3. 문제에서는 홀수일 때만 체크 하면 되지만 책에서는 짝수일 때도 체크하여 i+1(짝수), i+2(홀수) 인 expand중 최고를 체크

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''

        for i in range(len(s) -1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        
        return result
```