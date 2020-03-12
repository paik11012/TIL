

# 취뽀냥이  README

## http://i02a409.p.ssafy.io/



내 취업 정보(정보, 자기소개서, 인터뷰)를 한 번에 관리하는 페이지 입니다.

![intropng](./intropng.png)



## 목차

- 기술스택과 팀 소개
- 기획 의도
- ERD
- Frontend
- Backend
- 영상 링크
- 에필로그



##  1. 소개

### 기술스택 소개

[![alt text](https://img.shields.io/badge/java-v16.4.2-orange.svg?longCache=true&style=flat-square)](https://www.java.com/ko/) [![alt text](https://img.shields.io/badge/Springboot-gradle-9cf.svg?longCache=true&style=flat-square)](https://spring.io/projects/spring-boot) [![alt text](https://img.shields.io/badge/IntelliJ-2019.3.3-yellow.svg?longCache=true&style=flat-square)](https://www.jetbrains.com/ko-kr/idea/) [![alt text](https://img.shields.io/badge/MariaDB-10.4-blue.svg?longCache=true&style=flat-square)](https://mariadb.com/) 

[![alt text](https://img.shields.io/badge/vue.js-2.5.16-success.svg?longCache=true&style=flat-square)](https://vuejs.org/) [![alt text](https://img.shields.io/badge/@vue--cli-v4.1.2-green.svg?longCache=true&style=flat-square)](https://cli.vuejs.org/) [![alt text](https://img.shields.io/badge/VisualStudioCode-1.4-blueviolet.svg?longCache=true&style=flat-square)](https://code.visualstudio.com/) 



### 팀 소개

| 이름        | 역할                                                         |
| ----------- | ------------------------------------------------------------ |
| 박권응      |                                                              |
| 백민주      | Vue와 Vuetify 활용한 페이지 구성, Vuex 활용, Axios Rest-api를 이용한 백엔드와 통신 |
| 윤규희      |                                                              |
| 이다슬 팀장 |                                                              |



## 2. 기획의도

취업을 준비하는 사람 중 한 명으로서 취업정보를 한 번에 정리해주는 취업플랫폼이 있다면 편하지 않을까 생각을 해 보았다. 

1) 정보의 분산

개인적으로 면접 후기는 네이버 블로그에, 자기소개서는 컴퓨터 내 폴더에, 이력 정보는 엑셀 파일 관리하고 있으나 정보가 분산되어 있어 불편함을 느꼈다. 

2) 불편한 키워드 검색 기능

자기소개서를 쓸 때마다 기업이 요구하는 키워드에 맞게 글을 쓰기 위해 컴퓨터 자체의 검색기능을 활용해 불편한 키워드 검색을 할 수 밖에 없었다. 그래서 #키워드별 필터링 기능을 넣었다.

3) 글자수 파악의 어려움

내가 쓴 자기소개서의 글자를 직접 적어놓지 않는 이상 그 자기소개서 문항의 글자수를 파악하기 어려웠다. 

**따라서 자기소개서를 키워드로 관리해주면서 글자수까지 표시되어 자기소개서를 쉽게 쓸 수 있는, 더 나아가 이력과 면접후기 관리까지 할 수 있는 private한 사이트를 기획하게 되었다. **



## 3. ERD

테이블 8개 / 테이블끼리 user_id로 연결![ERD](./ERD.png)



## 4. 홈페이지 소개 및  Frontend - Vue.js 

### 홈페이지 구성

첫 접속 페이지(고양이 이미지를 클릭하면 사이트 소개 페이지로 넘어간다)

로그인 페이지(google과 naver를 이용한 social login 구현)

가입페이지(이메일 인증 구현)











삼성 소프트웨어 아카데미에서 배운 Vue를 활용해 프로젝트를 진행했다. 

### 컴포넌트 구성

```

```

### 페이지 구성

```
Views
|-----Homepage.vue
|-----MainPage.vue
|-----InterviewPage.vue
|-----MyPage.vue
|-----ResumePage.vue
|-----Teampage.vue
|-----Userinfo.vue
|-----AdminPage.vue
```

### 설치하기

```
https://bit.dev/joshk/vue-spinners-css/ring-loader
npm install
npm run serve
```

vue-router와 vuex의 이용



## 5. Backend

### 기술스택

- IntelliJ로 Spring boot Gradle 형식으로 개발
- JPA를 사용한 데이터베이스와의 연동
- RESTful 개발
- Swagger을 활용한 REST API 문서화 제공
- AWS의 ec2의 서버의 MariaDB 사용

### 배포 방법

1. IntelliJ를 각각의 운영체제에 맞는 버전을 다운 받는다. 
2. /web-9to6/build/libs 아래의 XX.jar 파일을 ec2 server로 전송(winSCP를 사용하거나 scp -i "T02A409.pem 파일 경로" -r ./dist ubuntu@15.164.244.244:/home/ubuntu/web-9to6/back/)
3. ec2 server에서 cd web-9to6/back/로 이동 후 nohup java -jar XX.jar & 커맨드 실행



## 6. 소개영상 링크(유튜브)

https://www.youtube.com/watch?v=1cyQnk2KHKc



## 7. 에필로그