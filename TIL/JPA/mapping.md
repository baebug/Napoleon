# Mapping

## 목차

1. [단방향 1:N](#단방향-1:N-(OneToMany))
2. [단방향 N:1](#단방향-N:1-(ManyToOne))
3. [양방향 1:N](#양방향-1:N)

---

상황 : 유저는 게시글을 0 또는 여러개 작성할 수 있다.

USER_TABLE

| user_seq | user_name | 
|---|---|
| 1 | baebug |
| 2 | ufr134 |

BOARD_TABLE

| board_seq | title | content | user_id | created_at | updated_at |
|---|---|---|---|---|---|
| 1 | JPA | JPA is ... | 1 | 2021-09-18 | 2023-01-19 |
| 2 | Spring | Spring is ... | 2 | 2022-03-17 | 2022-03-17 |
| 3 | Django | Django is ... | 1 | 2023-01-01 | 2023-01-17 |
  
</br>

## 단방향 1:N (OneToMany)

유저의 1명은 N 개의 게시글을 가질 수 있다.

```java
// UserEntity.java

@OneToMany(fetch=FetchType.LAZY, cascade=CascadeType.ALL)   // OneToMany 의 기본 fetch 전략은 LAZY 이다.
@JoinColumn(name="user_id") // (1)
private List<BoardEntity> boardList;
```

1. `@JoinColumn` 의 name 값은 `BOARD_TABLE` 에 있는 **User 연관 컬럼명**
    - fk 컬럼명

</br>
  
## 단방향 N:1 (ManyToOne)

N 개의 게시글은 유저 1명과 연관이 있다.

```java
// BoardEntity.java

@ManyToOne(targetEntity=User.class, fetch=FetchType.LAZY)
@JoinColumn(name="user_id") // (1)
private User user;
```

1. `@JoinColumn` 의 name 값은 `USER_TABLE` 의 **pk 와 연결될 컬럼명**
    - 그러니까 fk 컬럼명
  
</br>

## 양방향 1:N

```java
// UserEntity.java
@OneToMany(mappedBy="user") // (1)
private List<BoardEntity> boardList;

//BoardEntity.java
@ManyToOne(optional=false, fetch=FetchType.LAZY) // optional >> T: not null, F: nullable
@JoinColumn(name="user_id") // (2)
private UserEntity user;
```

1. `@OneToMany` 의 mappedBy 값은 BoardEntity 내부의 `User 클래스 변수명`
    - 반대쪽 매핑의 필드 이름

2. `@ManyToOne/@JoinColumn` 의 name 값은 `USER_TABLE` 의 **pk 와 연결될 컬럼명**
    - 그러니까 fk 컬럼명..

> 왜 이렇게 복잡하게 생겼지?

- 원래 단방향일때는 해당 클래스의 필드가 `어떤 컬럼` 을 통해 연결되는지 적혀있었다.

- 이게 양방향으로 확장되면 생각을 달리해야 하는데, 객체는 사실 양방향 연관관계라는 것이 없다.  
반면 DB 는 외래키(FK)를 통해 join이 가능한데, 이를 "양방향 연관관계를 맺는다"고 표현할 수 있다.

- 객체의 참조는 둘인데 외래키는 하나네? 그럼 누가 외래키를 관리해야 할까?

> 연관관계의 주인만이 외래키를 관리할 수 있다. 즉, FK 를 컬럼으로 가진 애가 주인.

- 주인이 아닌 쪽에서 `mappedBy` 속성을 사용한다.
    - 테이블에 FK 가 없는 애
- 1:N 관계에서 N 이 항상 FK 를 가진다!
    - `one == Collection Type 필드` 위 에 mappedBy
    - fk 가 있는 Table 에 해당하는 클래스-필드에 `@JoinColumn(name="fk컬럼명")` 어노테이션이 붙는다.

참고자료 : [[JPA] 연관관계 매핑 기초 #2 (양방향 연관관계와 연관관계의 주인)](https://velog.io/@conatuseus/%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84-%EB%A7%A4%ED%95%91-%EA%B8%B0%EC%B4%88-2-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84%EC%99%80-%EC%97%B0%EA%B4%80%EA%B4%80%EA%B3%84%EC%9D%98-%EC%A3%BC%EC%9D%B8)
