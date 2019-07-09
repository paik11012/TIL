## GIT

기본명령어

0. Git에 로그인

git config --global user.email "minju11012@gmail.com"

git config --global user.name "paik11012"

GIT 초기화

git bash 실행하고 계정 정보하기 삭제하기

$git config --global --unset credential.helper

$git system --global --unset credential.helper

git config –global –unset-all user.name

git config –global –unset-all user.email

$ git config user.email

1. Git 저장소 설정

git init

반드시 현재 디렉토리에  git을 사용하고 있는지, master가 없는지 확인 할 것

2. git add

git add는 현재 working directory에서 commit할 목록에 파일을 담아놓는 것이다. 그리고 그 목록은 index(staging area)라고 한다.

git add 홀더 이름 혹은 파일이름

3. git commit

현재 소스코드 상태를 저장하는 것, 스냅샷을 찍는 것과 동일하다.

staging are(git add를 추가한 파일이 담기는 곳)에 있는 내용을 이력으로 기록한다.

```
git commit -m "커밋메세지"
```

4. git status

git의 현재 상태를 확인한다

``` git status
git status
```

커밋할 목록에 담겨있는지 혹은 untracked인지, 커밋할 내역이 있는지 등 다양한 정보를 제공한다.

5. git log

현재까지 커밋된 모든 이력을 확인할 수 있다.

``` git log
git log
```

6. git 관리 취소하기

```
rm -f .git
```

상태 확인 git status, git remote -v

cd .. 상위 폴더로 가기

7. touch .gitignore 이용해 특정 텍스트 편집하기

vi .gitignore로 빔 에디터 이용

들어가서 esc-i누르면 편집 가능

무시하고 싶은 파일 목록 적기 ex) **.txt

그리고  esc누리고

:w저장q나가기

확인하기 vi .gitignore

(add한 것 되돌리기 git reset)



## 원격저장소 활용하기

1. 원격 저장소( remote repository)등록하기

``` gi
git remote add origin __경로__
```

origin이라는 이름으로 원격저장소를 등록한다.

최초에 한 번만 등록하면 된다. 

아래의 명령어로 현재 등록된 원격저장소를 확인할 수 있다.

```  
§ git remote -v
origin  https://github.com/paik11012/TIL.git (fetch)
origin  https://github.com/paik11012/TIL.git (push)
```

2. 원격 저장소에 올리기

origin이라는 원격저장소의 master 브랜치로 지금까지의 커밋 내역을 올려준다

``` 
§ git push origin master
```

3. 원격 저장소에 커밋한 것 가져오기

```
§ git pull origin master
```

4. 원격 저장소를 로컬에 복사하기 (clone)

다운받기를 원하는 폴더에서 git bash를 열고 위의 명령어를 입력. 경로는 github 초록버튼

``` 
§ git clone __경로__
```

ref: https://backlog.com/git-tutorial/kr/


