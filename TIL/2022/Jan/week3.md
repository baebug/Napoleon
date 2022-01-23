## 17일

---

### - 알고리즘

- `sorted( )` 는 첫 번째 인자로 들어온 iterable 한 데이터를 새로운 정렬된 리스트로 만들어서 반환해준다.
    - 때문에 set.sort() 는 안되지만, sorted(set) 은 가능하다.
- `list.index( )` 는 O(N) 의 시간복잡도를 갖기 때문에 for 문 안에 index 를 넣으면 O(N^2) 의 시간복잡도가 나온다.
    - cache 를 구현하더라도 index 를 사용하면 결국 최악의 상황에서는 O(N^2) 이 걸리므로 노노
    - enumerate 를 사용해 해결하였다.

```python
# 처음 코드 (시간초과)
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
s_arr = sorted(list(set(arr)))

for i in arr:
    print(s_arr.index(i), end=" ")


# cache 를 구현 (시간초과)
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
s_arr = sorted(set(arr))
myCache = {}

for i in s_arr:     # arr == s_arr 의 경우도 있으므로 안된다.
    myCache[i] = s_arr[i]

for i in arr:
    print(myCache[i], end=" ")


# 최종
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
s_arr = sorted(set(arr))
myCache = {}

for i, v in enumerate(s_arr):
    myCache[v] = i

for i in arr:
    print(myCache[i], end=" ")


# 그 외 추가 개선
ans = ' '.join(map(str, (myCache[i] for i in arr)))
print(ans)
```

### - 그 외

- 스프링 핵심 이론 기본 편 완강
- 이론적으로 대충 이해하고 넘어간 부분이 많지만, 현재로서는 최선이라고 생각
- 앞으로 스프링을 사용하면서 꾸준히 레퍼런스로 참고할 것

</br>

---

## 18일

---

### - 알고리즘

- 백트래킹(backtracking) 이란?
    - 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법
    - 깊이 우선 탐색(DFS, Depth-First Search) 기반
- DFS 와 백트래킹의 차이
    - DFS 는 가능한 모든 경로(후보)를 탐색하는 데 반해, 백트래킹은 노드가 유망(promising)하지 않은 경우 배제하고 해당 노드의 부모 노드로 되돌아간 후 다른 자손 노드를 검색한다.
    - 전문용어(?)로 가지치기(Pruning)라고 하는데, 불필요한 경로를 조기에 차단함으로써 경우의 수가 줄어든다.
- 해설
    - 기본적으로 재귀 함수의 형태를 보이기 때문에 모든 경우에 대해 탐색한다.
    - for 문 안에 있는 if 문을 통해 유망성을 판단하고, 유망하지 않은 경우 배제한다.
    - N 과 M 시리즈 외의 다양한 백트래킹 문제를 접해보고, 더 공부해봐야겠다.

```python
n, m = map(int, input().split())
arr =[]

def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n+1):
        if not i in arr:
            arr.append(i)
            dfs()           # len(arr) 가 m 일 때, return 으로 빠져나오고, arr.pop() 이 실행된다.
            arr.pop()

dfs()
```

### - SPRING

- servlet
    - `HttpServletRequest`, `HttpServletResponse` 를 통한 HTTP 요청 데이터와 응답 데이터 생성

</br>

---

## 23일

---

### - 주간 회고

- Spring MVC 가 너무 재밌어서 알고리즘 공부 잠시 보류
- MVC 1편 완강, 이후 학습 계획

```
1. 모든 개발자를 위한 HTTP (상태코드, 헤더 부분)
2. MVC 2편
3. JPA 활용 1편
4. JPA 기본편
5. JPA 활용 1편 복습
6. JPA 활용 2편 or 실전 JPA
```

- MVC 2편 이후, 개인프로젝트랑 병행해서 공부하기
    - 만들어보면서 모르는 부분, 디테일한 부분 잡기 (기본편, MVC 1편 참고)
    - 고민하고, 깊게 공부하고, 포스팅 하기 (언제든 참고할 수 있게 개념의 전체적인 그림)
- 이후 JPA 들으면서 DB 연동 등등