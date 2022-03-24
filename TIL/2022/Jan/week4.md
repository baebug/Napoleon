## 24일

---

### - Spring

- 외부의 파일을 복사해왔는데 적용이 잘 안되면, 프로젝트 경로의 `out` 폴더를 지운 뒤 재실행

```java
@Component("helloBean")
    static class HelloBean {
        public String hello(String data) {
            return "Hello " + data;
        }
    }
```

- `@Component` 애노테이션이 붙은 HelloBean 클래스의 빈 이름을 helloBean 이라고 설정해주는데 원래 빈 이름은 default 값이 클래스의 이름을 따라가지 않는가?(당연히 첫글자는 소문자) 궁금증이 생겼다.
- 실제로 `value = "helloBean"` 부분을 지우니 `NoSuchBeanDefinitionException` 이 발생하였고, 원인을 찾기 위해 모든 Bean 을 조회하는 init 메서드를 `@PostConstruct` 애노테이션을 붙여 작성하였다.

```java
@PostConstruct
    public void init() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(HelloBean.class);
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();
        for (String beanDefinitionName : beanDefinitionNames) {
            log.info("beanDefinitionName = " + beanDefinitionName);
        }
    }
```

- 출력 결과

```java
// value 값을 넣어준 경우
beanDefinitionName = helloBean

// value 생략
beanDefinitionName = basicController.HelloBean
```

</br>

---