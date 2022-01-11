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

