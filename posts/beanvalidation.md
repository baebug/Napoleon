---
title: Bean Validation
description: template
date: 2022-04-01 15:23:00 +09:00
categories:
  - java
  - spring
status: 작성중
last_modified_at: 2022-04-02 22:27:00 +09:00
---

## Bean Validation

### Bean Validation 이란?

객체(domain)의 특정 필드에 대한 검증 로직은 빈 값(blank)인지 아닌지, 조건 범위를 벗어나는지 등의 일반적인 로직이 많은데, 이러한 검증 로직을 여러 프로젝트에 적용할 수 있게 공통화, 표준화하여 애노테이션으로 편리하게 적용할 수 있도록 개발한 것
Bean Validation 은 특정한 구현체가 아니라 검증 애노테이션과 여러 인터페이스의 모음이다. 그 중 일반적으로 사용하는 구현체의 이름이 'hibernate-validator' 이며, ORM 이랑은 관련없음.

### 시작하기

build.gradle 에 의존관계를 추가해야 한다.
  - `implementation 'org.springframework.boot:spring-boot-starter-validation'`

추가된 라이브러리들
  - `jakarta.validation-api ~` : 인터페이스 제공
  - `hibernate.validator ~` : 구현체

### 사용법

객체의 필드에 애노테이션을 붙이면 된다. 아주 간단하죠?

[검증 애노테이션 모음](https://docs.jboss.org/hibernate/validator/6.2/reference/en-US/html_single/#validator-defineconstraints-spec)

검증기를 생성하고 사용

```java
ValidatorFactory factory = Validation.buildDefaultValidatorFactory();
Validator validator = factory.getValidator();

Set<ConstraintViolation<Item>> violations = validator.validate(item);
iter -> soutv
```

이후 스프링과 통합하면 이런 코드를 직접 작성하지 않는다.
  - `spring-boot-starter-validation` 라이브러리를 넣으면 자동으로 Bean Validator 를 인지하고 글로벌 Validator 로 등록하기 때문에 사용 시 `@Validated` 만 적용하면 된다.
  - 검증 오류가 발생하면 `FieldError`, `ObjectError` 를 생성하여 `BindingResult` 에 담아준다.

### 오류코드

기본적으로 제공하는 오류 메시지를 변경하는 방법

1. `messageSource` 에서 메시지를 찾는데, `MessageCodesResolver` 를 통해 메시지 코드가 생성되는 규칙이 있다.
  - @애노테이션 이름.객체명.필드명 (`NotBlank.item.itemName`)
  - @애노테이션 이름.필드명 (`NotBlank.itemName`)
  - @애노테이션 이름.타입명 (`NotBlank.java.lang.String`)
  - @애노테이션 이름 (`NotBlank`)
2. 애노테이션의 `message` 속성 사용
  - `@NotBlank(message = "공백X")`

### ObjectError

특정 필드에 대한 검증(`FieldError`) 외 오브젝트 관련 검증(`ObjectError`)은 어떻게 처리하는가.

1. `@ScriptAssert()` 를 사용한다.
  - 제약이 많고 복잡해서 비추천
  - 검증 기능이 해당 객체의 범위를 벗어나는 경우에 대한 대응이 어렵다.
2. Java 코드로 작성한다.

### 한계점

동일한 모델 객체지만 상황에 따라 다른 요구사항이 필요할 수도 있다. (등록할 때, 수정할 때 등)

해결방법
1. BeanValidation 의 groups 기능을 사용한다.
  - groups 기능을 위한 구별용 인터페이스를 만든다.
  - groups 속성을 사용하여 애노테이션을 분리한다.
  - Controller 의 `@Validated` 애노테이션에 사용할 그룹을 넣어준다.

```java
@NotBlank(groups = {SaveCheck.class, UpdateCheck.class})

@PostMapping("/add")
public String add(@Validated(SaveCheck.class) @ModelAttribute Item item, ...) {
  //...
}
```

2. 객체를 직접 사용하지 않고, 폼 전송을 위한 별도의 모델 객체를 만들어 사용한다.
  - 모델 객체에 필드별로 알맞은 애노테이션이 입력된 폼전송객체(`ItemSaveForm`, `ItemUpdateForm`)를 생성한다.
  - `ModelAttribute` 를 통해 폼 객체를 바인딩한다.
  - 전달된 `form` 을 `Item` 으로 변환하는 과정을 거친다.

```java
Item item = new Item();
item.setItemName(form.getItemName());
...
item.setQuantity(form.getQuantity());
```

### ModelAttribute

```java
public String add(@Validated @ModelAttribute("item") ItemSaveForm form, BindingResult bindingResult, ...) {
  ...
}
```

를 하면 발생하는 과정들

1. `ItemSaveForm` 객체 form 을 생성 후 item 이라는 이름으로 MVC Model 에 추가하고 view 단으로 넘긴다.
  - `Model.addAttribute("item", form)`
2. view 단에서 입력되는 값 (`th:object = "item"`) 들을 바인딩한다.
3. 검증하고 오류가 발생하면 `BindingResult` 에 담는다.

### RequestBody

`@ModelAttribute` 말고 `@RequestBody` 에도 적용 가능하다.

차이점
- `@ModelAttribute` 는 각각의 필드 단위로 정교하게 바인딩이 적용된다. 특정 필드가 바인딩 되지 않아도 나머지 필드는 정상 바인딩 되고, `Validator` 를 사용한 검증도 적용할 수 있다.
- `@RequestBody` 는 HttpMessageConverter 단계에서 JSON 데이터를 객체로 변경하지 못하면 이후 단계가 진행되지 않고 예외를 뱉는다. 이러한 경우, `Controller` 도 호출되지 않고, `Validator` 도 적용할 수 없다.