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