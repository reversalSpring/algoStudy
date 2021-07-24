# 4장 빅오, 자료형

## <a name='TOC'>목차</a>
0. [목차](#TOC)
1. [빅오(Big-O)](#bigO)
2. [자료형](#datatypes)



## <a name='bigO'>빅오(Big-O)</a>
### 1.1 정의
  - 점근적 실행 시간을 표기하는 방법 중 하나(상한)
      - 시간 복잡도(TC) : 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명
      - 하한을 나타내는 빅오메가(Ω), 평균을 의미하는 빅세타(Θ)도 있음
      - [시간 복잡도와 알고리즘](https://velog.io/@bathingape/Time-Complexity%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84)
      - [Python의 시간 복잡도 총정리](https://chancoding.tistory.com/43)

### 1.2 분할 상환 분석
  - [Amortized Analysis](https://hcn1519.github.io/articles/2017-05/amortized_analysis)

### 1.3 병렬화
  - [Python 병렬처리를 통한 연산속도 개선](https://yganalyst.github.io/data_handling/memo_17_parallel/)
  - [Parallel Processing in Python](https://www.machinelearningplus.com/python/parallel-processing-python/)
  - [5 Step Guide to Parallel Processing in Python](https://medium.com/swlh/5-step-guide-to-parallel-processing-in-python-ac0ecdfcea09)

## <a name='datatypes'>자료형</a>
### 2.1 Python의 자료형
<table>
	<tr>
		<th>분류</th>
		<th>클래스</th>
		<th>비고</th>
	</tr>
	<tr>
		<td>None</td>
		<td>None</td>
		<td>class None Type</td>
	</tr>
	<tr>
		<td rowspan="3">숫자</td>
		<td>정수</td>
		<td>class int</td>
	</tr>
	<tr>
		<td>Boolean</td>
		<td>class bool</td>
	</tr>
	<tr>
		<td>실수</td>
		<td>class float</td>
	</tr>
	<tr>
		<td rowspan="4">시퀀스</td>
		<td>문자열</td>
		<td>class str</td>
	</tr>
	<tr>
		<td>튜플</td>
		<td>class tuple</td>
	</tr>
	<tr>
		<td>바이트</td>
		<td>class bytes</td>
	</tr>
	<tr>
		<td>리스트*</td>
		<td>class list</td>
	</tr>
	<tr>
		<td>집합형</td>
		<td>집합</td>
		<td>class Set</td>
	</tr>
	<tr>
		<td>맵핑</td>
		<td>딕셔너리*</td>
		<td>class dict</td>
	</tr>
</table>

#### 2.1.1 숫자
  1. 정수형 **int**와 **bool**
      * int
         * Python 2.x 까지는 int와 long이 별도로 제공됐으나, 3.x부터는 int 단일형으로 통합됨
         * int의 임의 정밀도
     
      * bool
         * 엄밀히 따지면 논리 자료형임 - 1(True) / 0(False)
         * object > int > bool
	 
  2. 실수형 **float**

#### 2.1.2 맵핑
  1. **딕셔너리**
      * Key-Value 쌍 (버전 3.7부터는 입력 순서가 유지됨)
      * 선언
	      ```python
	      # 방법 1
	      a = {}
	      a['key1'] = 'val1'
	      
	      # 방법 2
	      b = {'key1':'val1', 'key2':'val2', .... ,'keyN':'valN'}
	      ```
		  
#### 2.1.3 집합
  1. Set
      * 중복된 값을 갖지 않으며, 입력 순서가 유지되지 않는다.
      * 선언
	    ```python
		# 방법 1
		a = set()
		a.add(1)
		  
		# 방법 2
		a = {1, 3, 5, 7, 7, 7}
		```
      * 중복된 값이 들어가 있는 경우, 알아서 하나만 남긴다.

#### 2.1.4 시퀀스
  1. 불변 - str, tuple, bytes
      - str
	      ```python
	      # 선언
	      a = 'string'
	      
	      # 숫자형/문자형 형 변환
	      num1 = 3.333
	      num2 = 6
	      str1 = '27'
	      print(num1 + num2)  # 9.333
	      print(num1 + str1)  # 오류
	      print(num1 + int(str1))  # 30.333
	      print(num2 + float(str1))  # 33.0
	      print(str(num1) + str1)  # 3.33327
	      print(str(num1), str1)  # 3.333 27
	      ```
      - tuple
          - 선언
	     ```python
	     # 선언
	     a = (1, 2, 3)
	     b = (1,)  # 아이템을 하나만 넣을 때는 끝에 꼭 comma를 넣어야 튜플로 인식한다!
	     ```
          - list와의 비교
	      ```
	      - (공통점) 연산 : 인덱싱, 슬라이싱 등이 가능함
	      - (차이점) 선언 : list는 []를, tuple은 ()을 사용
	      - (차이점) 불변성 : tuple은 값을 변경하는 것이 불가능(immutable) → tuple은 그 자체를 딕셔너리의 key 값으로 사용 가능
	      - Q) list가 있는데 왜 tuple이 필요해요?
	        A) https://www.quora.com/What-is-the-point-of-a-tuple-in-Python-Why-not-just-use-a-list-and-not-change-it
	      ```
      - bytes
          - 선언
	     ```python
	     a = b'str 앞에 b만 붙이면 됨'  # SyntaxError: bytes can only contain ASCII literal characters.
	     a = b'Just add b'  # <class 'bytes'>
	     ```
          - [너저분했던 Python 2.x 에서의 역사](https://medium.com/better-programming/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686)
          - [str 과의 비교](https://mino-park7.github.io/effective%20python%20study/2018/09/06/betterway3-bytes-str-unicode/)
	 
  2. 가변 - **list**
      - list
          - 선언
	      ```python
	      # 방법 1
	      a = []
	      a.append(0)
	      a.append('str')
	      a.append(b'bytes')
	      print(a)  # [0, 'str', b'bytes']
	      
	      # 방법 2
	      a = [1, 'sleepy', 3.53]
	      print(a)  # [1, 'sleepy', 3.53]
	      ```

### 2.2 원시 타입
    SKIP ("Python은 원시 타입의 속도를 포기하는 대신 객체의 다양한 기능과 편의성을 택했다")
### 2.3 객체
#### 2.3.0 (책에 없는?) 읽으면 좋을 내용
  1. [객체란](https://wikidocs.net/20457)
  2. [Python의 객체 참조, 가변성, 재사용](https://medium.com/humanscape-tech/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-%EA%B0%9D%EC%B2%B4-%EC%B0%B8%EC%A1%B0-%EA%B0%80%EB%B3%80%EC%84%B1-%EC%9E%AC%ED%99%9C%EC%9A%A9-cd0afc889d77)
  3. [참조, 얕은 복사, 깊은 복사](https://hamait.tistory.com/844)
  3. [Python과 다른 프로그래밍 언어들 비교](https://pybo.kr/pybo/question/detail/112/)
#### 2.3.1 불변 객체
  1. 속하는 자료형
      - bool/int/float
      - str/tuple/bytes
  2. 하지만 a=0에서 a=10이 가능하지 않나요?
      - 보이는 것과 다르게 변수가 참조하는 주소에 담겨져 있는 값이 변한 게 아니라, 변수가 기존 객체와는 다른 새 객체를 참조하게 된 것
#### 2.3.2 가변 객체
  1. 속하는 자료형
      - list
      - set
      - dict
  2. 참조(Reference) 방식 비교 (w/ C++)
      - C++ : 참조하는 객체의 값이 달라진다 (=101호의 거주자 변경)
      - Python : 참조하는 객체가 달라진다 (=101호가 아닌 102호로 이사)
  3. is와 ==
      - is : 메모리 주소를 비교
      - == : 값을 비교

#### 2.3.3 속도
    SKIP

