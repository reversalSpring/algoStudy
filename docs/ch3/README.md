### indent

파이썬은 인덴트(4칸 들여쓰기) 기반 

### Naming Convention

underscore(_) 기반의 snake_case를 사용

### Type Hint

v3.5부터 사용할 수 있다.

```python
a: str = "1"
b: int = 1

def function(a: int) -> bool:
	pass
```

명시적인 선언일 뿐이며 강제 규약이기 아니기 때문에 동적으로 할당이 가능, 주의해야 함

### List Comprehension

⇒ 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문

자바 보다 빠르게 map, filter 등의 함수형 기능을 지원하고 람다 표현식을 지원함

```python
list(map(lambda x: x + 10, [1,2,3]))
# [10+1, 10+2, 10+3]
[11, 12, 13]

# No list comprehension
a = []
for n in range(1, 10+1):
	if n % 2 == 1:
		a.append(n * 2)

# list comprehension
[n * 2 for n in range(1, 10+1) if n% 2 == 1]

[2, 6, 10, 14, 18]

a = {}
for key, value in orginal.items():
	a[key] = value

a = {key: value for key, value in original.items()}
```

간단한 라인은 가독성을 향상시키지만 너무 줄이면 오히려 가독성이 떨어진다.

### Generator

루프의 반복(iteration) 동작을 제어할 수 있는 루틴 형태

`yield` 구문을 사용하면 제너레이터를 리턴할 수 있다. return과 달리 함수가 완전 종료되지 않는다. 실행 중인 값을 내보내다.

다음 값을 호출하려면 `next()` 사용

```python
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

def generator():
    yield 1
    yield 'Hello'
    yield True

g = generator()
print(next(g)) # 1
print(next(g)) # Hello
print(next(g)) # True
```

### Range

내부적으로 제너레이터 방식을 활용하는 대표적인 함수가 `range()`가 있다. for loop에서 사용할 경우 내부적으로 제너레이터의 next()를 호출하듯 매번 다음 숫자를 생성한다. v2.x 에서는 리스트를 반환

```python
list(range(5))

type(range(10)) # <class 'range'>
```

이미 생성된 값을 담고 있느냐 or 즉각 생성해야 하느냐 ⇒ 메모리 점유율 차이 존재

### enumerate

순서가 있는 list, set, tuple 자료형을 인덱스를 포함한 enumerate 객체로 리턴

```python
>>> a =  ["a", "b", 'c', 'd', 'e']
>>> enumerate(a)
<enumerate object at 0x105bfd640>
>>> list(enumerate(a))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

for i, v in enumerate(a):
    print(i, v)
```

5 / 3 

v2 : 1

v3 : 1.6666

### Print

```python
print("a", "b", sep=',')

print("a", end='')
for i in range(5):
    print('*', end='') # *****

a = ['a', 'b', 'c']
print(' '.join(a))
>>> a b c

idx = 1
fruit = 'Apple'

print('{}: {}'.format(idx+1, fruit)
print(f'{idx+1}: {fruit}')
# 2: Apple
```

### locals

로컬 심볼 테이블 딕셔너리를 가져오는 메소드, 디버깅할 때 많이 사용, 업데이트도 가능

```python
import pprint
pprint.pprint(locals())

```

### Queue

```python
import queue
q = queue.Queue()
q = queue.PriorityQueue()

```


### String & Unicode
```python
print( type('hello') )
print( type(u'hello') )
# <type 'str'>
# <type 'unicode'>
```

```python
print( type('hello') )
print( type(u'hello') )
# <class 'str'>
# <class 'str'>
```

### long == int
```python
print( 2**30 )
print( type(2**30) )
print( 2**100 )
print( type(2**100) )
# 1073741824
# <class 'int'>
# 1267650600228229401496703205376
# <class 'int'>
```

ref : https://geekhub.co.kr/blog/translation-python37-new-features/

### collections
- collections.Counter : 아이템에 대한 갯수를 계산해서 딕셔너리르 반환
- collections.OrderedDict()
- collections.defaultDict() : 존재하지 않는 키를 조회할 경우 에러 대신 디폴트 값 반환
- collections.deque : double ended queue

