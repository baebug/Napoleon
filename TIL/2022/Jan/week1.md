# 1월 1주 차

## 3일

---

### - 알고리즘

- 기본 수학 단계로 들어왔는데 진짜 수학적인 사고력을 요하는 문제들이 나오기 시작했다.
- 등차수열처럼 단계적으로 수가 증가하고 어떤 숫자의 구간을 찾는 문제?들

```python
# ex. 1/1, 1/2, 2/2, 1/3, 2/3, 3/3, 1/4, ... 일 때, n번 째 수는 무엇인가?
idx = 0

while n > 0:
	idx += 1
	n -= idx
	
print(idx)

# n = 3 이면 idx = 2
```

- 이런 식으로 `while` 을 사용해서 구현했는데, 괜찮은 방법인 것 같다.

## 4일

---

### - 알고리즘

- 몫과 나머지를 사용할 때, 나누어 떨어지는 경우에 대해서 유의해야 함.
```python
# Q. 10250

if N % H == 0:
	h = H
	w = N // H
else:
	h = N % H
	w = N // H + 1
```
- 시, 분, 초 처럼 한 자릿수 일 때, 두 자리로 포매팅
```python
# w1 은 정수 데이터지만, w2는 문자열로 반환된다.

w2 = '{0:02d}'.format(w1)
```
- 재귀적으로 알고리즘을 풀어야 할 때(ex. 피보나치), array 에 저장해서 효율을 높일 수 있다.
```python
# Q. 2775
# 전역 변수로 array 를 선언하고, 함수에서 접근하여 저장한다.

def cal_people(floor, column):
    sum = 0
    if floor == 0: return column

    if apt[column - 1][floor - 1] == 0:
        for i in range(1, column + 1):
            sum += cal_people(floor - 1, i)
        apt[column - 1][floor - 1] = sum
    
    return apt[column - 1][floor - 1]

for _ in range(t):
    k = int(input())
    n = int(input())
    apt = [[0 for _ in range(k)] for _ in range(n)]
	cal_people(k, n)
```

### - awt

- GUI 프로그래밍에 필요한 다양한 컴포넌트를 제공해주는 도구
	- 웹을 벗어난 GUI 프로그래밍은 거의 처음이라 신기하다.
- ['자바킹'님 블로그 - LayoutManager](https://m.blog.naver.com/javaking75/140157948347)