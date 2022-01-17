## 11일

---

### - 알고리즘

- 재귀 파트에 들어왔는데 어렵다..
- 재귀 함수의 경우 parameter 로 무엇을 넘겨줄 지를 잘 생각해야 함. 문제가 복잡해지면 주로 `list` 를 넘겨주더라.
- `dictionary` 로 cache 를 구현해 실행 시간을 줄이는 방법도 있다.
- 별찍기의 경우 구조는 파악했으나 `print( )` 로 구현했더니 계속 줄바꿈 이슈가 생겼고, 도저히 해결 방안이 떠오르지않아 구글 찬스를 사용했다.
- 얘는 다시 나오면 풀 자신이 없어서.. 좀 더 봐야 할 듯

```python
# 재귀 - 별찍기 (2447)

def star(n, arr):
    matrix = []

    if n == 3:
        return arr
    else:
        for i in arr:
            matrix.append(i * 3)
        for i in arr:
            matrix.append(i + " " * len(arr) + i)
        for i in arr:
            matrix.append(i * 3)
        return star(n//3, matrix)

first = ["***", "* *", "***"]
n = int(input())        

ans = star(n, first)

for i in ans:
    print(i)
```

- 하노이 탑의 경우 무지성 `print( )` 로 구현했더니, 실행 속도가 950ms (ㅋㅋ) 가 나왔다.
- cache 구현의 경우 80ms 까지 줄어들었다.

```python
# 재귀 - 하노이 탑 이동 순서

# 무지성 print  (948ms)
def hanoi(n, start, end):
    other = 6 - (start + end)
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, other)
        print(start, end)
        hanoi(n - 1, other, end)

n = int(input())

print(2 ** n - 1)
hanoi(n, 1, 3)

# Cache  (80ms)
myCache = {}

def hanoi(n, start, end):
    other = 6 - (start + end)
    if n == 1:
        return str(start) + " " + str(end)
    if (n, start, end) in myCache:
        return myCache[(n, start, end)]
    
    tmp = [hanoi(n - 1, start, other), str(start) + " " + str(end), hanoi(n - 1, other, end)]
    myCache[(n, start, end)] = '\n'.join(tmp)
    return myCache[(n, start, end)]

n = int(input())

print(2 ** n - 1)
print(hanoi(n, 1, 3))
```

- `dictionary` 에서 key 값의 존재 여부를 확인하려면 `in` 을 사용한다.

```python
_dict = {(2, 3, 4): [3, 4, 5]}

if _dict[(1, 2, 3)]:        # X , KeyError 가 발생한다.

if (1, 2, 3) in _dict:      # O , False 가 반환된다.
```

</br>

---

## 12일

---

### - 알고리즘

- 브루트 포스는 무식하게 구현해도 돼서 마음이 편했다.
- 근데 뒤에서 좀 더 효율적인 방법으로 구현하는 문제가 나오지 않으면, 따로 해봐야 함.

### - 배이괜

일단 twitch 사이트를 끊었다. `$ sudo vi /private/etc/hosts`
나태한 것도 문제지만, 요즘은 나태함에 대한 위기의식도 잘 안 느껴짐. 이 정돈 아니었는데 쩝..
코테3 이라도 꾸준히 해서 다행인데 일단 근본적인 원인을 찾고 해결 방안을 모색해야 함.

- 원인
    - 요즘 공부하던 파트가 너무 이론적으로 파고들면서 직접적으로 구현하는 게 거의 없어짐 -> 노잼
    - 자낳대랑 \-메\-가 하필 시기가 겹쳐서 너무 재밌게 봄 -> 생활 패턴 무너짐
- 해결
    - 트우치 끊기
    - 한 과목을 끝내려고 너무 그것만 보지 말고 좀 돌려가면서 공부해야 할 듯. 시간대별 or 요일별
    - 주말 토이프로젝트. **필요성을 느끼며 공부하자.**

</br>

---

## 14일

---

### - 알고리즘

- 카운팅 정렬
    - 각 수별로 count 해서 `counting_arr` 에 저장하고, 그걸 바탕으로 `output_arr` 를 작성한다.
    - 백준에 있는 카운팅 정렬 문제는 메모리 및 시간 제한 때문에 `input_arr` , `output_arr` 없이 구현해야 된다.
    - 그냥 구현했을 때는 약 12000ms 였지만, while 문을 이용해서 1000개 씩 끊어주니 4000ms 로 시간이 줄어들었다.
    - 메모리와 시간의 적절한 타협이 필요하다. - 경험

```python
N = int(input())
arr = [0] * 10001                   # idx 가 0 부터 10000 까지

for _ in range(N):
    arr[int(input())] += 1          # 들어오는 즉시 count

for i in range(len(arr)):
    if arr[i]:
        while arr[i] > 1000:
            print((str(i) + '\n') * 1000)
            arr[i] -= 1000
        print((str(i) + '\n') * arr[i])
```

- 통계학
    - 문제의 최빈값에서 개고생했다. (심지어 마지막에 다 구현했는데 계속 안되다가 어느 순간 통과함..)
    - 최빈값이 두 개 이상일 때, 두 번째로 작은 값을 출력하라는 조건 때문에 더 복잡해졌다.
    - 최빈값은 `count( )` 로도 구현할 수 있지만, collections 라이브러리의 `Counter` 를 이용하면 더 빠르고 간편하다.

```python
# count
tmp = [arr.count(i) for i in arr]
rest_list = [arr[i] for i, e in enumerate(tmp) if e == max(tmp)]
result = (sorted(set(rest_list)))
if len(result) >= 2:
    return result[1]
return result[0]

# from collections import Counter
cnt = Counter(arr)
mode = cnt.most_common()
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        return mode[1][0]
return mode[0][0]
```

</br>

---

## 15일

---

### - 알고리즘

- 좌표 정렬하기 문제에서 처음 구현한 코드
    - 좌표의 수 N 을 입력받고 (x, y) 형태로 바꿔서 li 에 append 해줬다.
    - 그냥 `sort( )` 해봤는데 알아서 우선순위를 가지고 정렬이 되더라.
    - 다시 for 문으로 순회돌면서 print 해줬다.

```python
import sys

input = sys.stdin.readline

N = int(input())
li = []

for i in range(N):
    li.append(list(map(int, input().split())))

li.sort()

for i in li:
    print(i[0], i[1])
```

- 최적화 및 응용(정렬 기준 변경) 구현 코드
    - 좌표의 수 N 을 입력받고 list comprehension 을 이용해 바로 li 만들어준다. (`strip( )` 을 쓰지 않고 개행문자까지 넣어주는 게 포인트)
    - `sort( )` 함수에서 `key` 와 `lambda` 를 이용해 특정 기준으로 정렬을 실행한다. (우선순위 높은 기준을 나중에)
    - li 의 원소에 개행문자가 포함되어있기 때문에 빈칸 없이 join 해준다.

```python
import sys

input = sys.stdin.readline

N = int(input())
li = [input() for _ in range(N)]

li.sort(key=lambda x: int(x.split()[1]))
li.sort(key=lambda x: int(x.split()[0]))

# 이런 방법도 있다.
# li.sort(key=lambda x: tuple(map(int, x.split())))   # tuple 이 list 보다 빠르다.

# li = ['1 -1\n', '1 2\n', '2 2\n', '3 3\n', '0 4\n']
print(''.join(li))
```

</br>

---

## 16일

---

### - 주간 회고

- 알고리즘 외 자바의 정석, SPRING 핵심 원리 기본편, HTTP 웹 기본 지식 등 공부함
- 핵심 원리랑 HTTP 빨리 끝내고 (월, 화?) MVC 드가자
- 금주 싸이클 너무 많이 쉬었는데, 담주는 열심히 타자..
- 주말 토이프로젝트 설계 마무리 하기