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

</br>
</br>
---

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

</br>
</br>
---

## 5일

---

### - 알고리즘

- 수학적인 사고력을 요하는 문제에서는 구현부터 들어가지 말고 좀 더 차근차근 생각해보는 게 좋을 듯.. 결국 다시 풀게 되더라.
- 구현 자체의 어려움은 없고, 결국 논리적으로 해결법을 떠올리느냐의 문제라 오늘은 딱히 적을 게 없다.

### - awt

- MENU Component
- LayoutManager
- Event Handling
    - Event Source, Event Listener, Event Handler
- applet: `Deprecated`

### - Singleton pattern

- 첨에 AppConfig 인스턴스 만들어서 memberService 객체를 호출했는데, 그러면 부를 때마다 객체를 새로 생성하고, 소멸시키느라 메모리가 낭비된다.
```java
AppConfig appConfig = new AppConfig();

/* 둘이 다른 객체임 */
MemberService memberService1 = appConfig.memberService();
MemberService memberService2 = appConfig.memberService();
```
- 그래서 사용하는 디자인이 싱글톤 패턴이다.
    - 클래스의 인스턴스가 딱 1개만 생성되는 것을 보장.
    - static 영역에 객체 인스턴스를 미리 하나 올려두고 공유해서 사용한다.
```java
public class SingletonService {
    /* static 영역에 객체를 딱 1개만 생성해둔다. */
    private static final SingletonService instance = new SingletonService();

    /* 객체의 인스턴스가 필요하면 이 static 메서드를 통해서만 조회가 가능하다. (public) */
    public static SingletonService getInstance() {
        return instance;
    }

    /* private 생성자를 통해 외부에서 new 키워드로 객체 생성을 못하게 막는다. */
    private SingletonService() { }

    public void logic() {
        System.out.println("싱글톤 객체 로직 호출");
    }
}
```
- 구현하는 코드 자체도 복잡할뿐더러, 여러 가지 문제점이 있다.
    - 클라이언트가 `SingletonService` 라는 구체 클래스에 의존하기 때문에 DIP를 위반하며, OCP 원칙도 위반할 가능성이 높다.
    - 유연성이 낮아 내부 속성을 변경하거나 초기화하기 어렵고, 테스트 또한 어렵다.
    - private 생성자때문에 자식 클래스를 만들기 어렵다.
    - 안티 패턴으로 불리기도 한다. (많이 사용되지만 비생산/비효율적인 코드를 일컫는 말)

### - Singleton Container

- 이전에 학습한 스프링 빈이 바로 싱글톤으로 관리되는 빈이다.
- 객체 인스턴스를 1개로 관리할 뿐만 아니라, 위에서 상술한 문제점을 모두 보완하였다.
```java
ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

/* 둘이 같은 객체임 */
MemberService memberService1 = ac.getBean("memberService", MemberService.class);
MemberService memberService2 = ac.getBean("memberService", MemberService.class);
```
- **(진짜 중요)** 같은 객체 인스턴스를 공유하기 때문에 `stateful` 하게 설계하면 안된다! 
```java
// stateful
public class statefulService {
    private int price;

    public void order(String name, int price) {
        System.out.println("name = " + name + ", price = " + price);
        this.price = price;
    }

    public int getPrice() {
        return price;
    }
}

// stateless
public class statelessService {
    public int order(String name, int price) {
        System.out.println("name = " + name + ", price = " + price);
        return price;
    }
}
```

</br>
</br>
---

## 6일 ~ 7일

---

### - 알고리즘

- 소수 판별의 경우, `에라토스테네스의 체` 등 이론적인 내용은 다 알고 있었는데 실제로 구현을 안해봐서 많이 헤매고, 시간 초과가 발생했다.
- 핵심 개념 1 : 어떤 수 n 이 주어졌을 때, n 의 제곱근 보다 작은 수로 안나누어지면 n 은 소수이다.
```python
# 중요 포인트 1
# 에라토스테네스의 체 만드는 법

max_n = 10000 # 최대로 주어지는 자연수
eratos = [False, False] + [True for _ in range(max_n - 1)]  # index 가 0 부터 max_n 까지 생긴다.

for i in range(2, int(max_n ** 0.5) + 1):                   # 핵심 개념 1
    if eratos[i]:
        for j in range(i * 2, max_n + 1, i):
            eratos[j] = False

# index 가 소수인 경우에만, eratos[index] = True 이다.
```

- 소인수분해의 경우 2 부터 나누면서 올라가기 때문에, div 가 소수인지 따로 확인할 필요가 없다. (이미 다 쪼개짐)
```python
def solve(n):
    d = 2
    while d * d <= n:                   # 핵심 개념 1
        if n % d == 0:
            print(d)
            n //= d
        else:
            d += 2 if d > 2 else 1      # 짝수인 소수는 2 뿐이다.
    if n > 1:
        print(n)
```

- 위 소인수분해 코드에서 안나눠지는 경우를 찾으면 소수판별이 가능하다.
```python
def isPrime(n):
    if n == 1: return False
    
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        else:
            d += 2 if d > 2 else 1
    return True
```

</br>
</br>
---

## 8일

---