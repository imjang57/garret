Title: Git Submodule
Date: 2017-12-16
Modified: 2017-12-16
Tags: git
Slug: git-submodule
Authors: imjang57
Summary: Git Submodule 사용법

# Git submodule

Git 서브모듈(Git submodule)은  Git 저장소(Git Repository)에 다른 Git 저장소를 포함시키기 위한 도구이다. 이렇게 다른 저장소를 저장소 내부에 추가하여도 각 저장소는 독립적으로 관리된다. 보통 서브모듈을 포함하는 저장소를 슈퍼프로젝트(Super-project)라고 한다.

## Add submodule

서브모듈을 추가하려면 저장소에서 다음과 같이 실행하면 된다. 예를 들어 서브모듈로 추가하려는 저장소의 이름을 `yourtheme` 라고 하자.

```bash
$ git submodule add https://github.com/imjang57/yourtheme theme/yourtheme
```

`theme/yourtheme`에 서브모듈 저장소가 생성된다. 슈퍼프로젝트에서 `git status` 명령을 실행하면 `.gitmodules` 파일과 `theme/yourtheme` 파일이 새로 생성된 것을 확인할 수 있다.

```bash
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      new file:   .gitmodules
#      new file:   theme/yourtheme
#
```

`.gitmodules` 파일의 내용은 다음과 같다.

```
[submodule "theme/yourtheme"]
    path = theme/yourtheme
    url = https://github.com/imjang57/yourtheme
```

그리고 `theme/yourtheme` 파일을 확인하면 다음과 같이 출력된다.

```bash
$ git diff --cached theme/yourtheme
diff --git a/theme/yourtheme b/theme/yourtheme
new file mode 160000
index 0000000..08d709f
--- /dev/null
+++ b/theme/yourtheme
@@ -0,0 +1 @@
+Subproject commit 08d709f78b8c5b0fbeb7821e37fa53e69afcf433
```

`git diff` 명령의 결과가 파일의 내용이 아니라 `Subproject commit 08d709f78b8c5b0fbeb7821e37fa53e69afcf433` 와 같이 출력되는 것을 확인할 수 있다. 이것은 Git이 `theme/yourtheme`를 서브모듈로 인식해서 서브모듈의 어느 커밋(commit)을 참조하고 있는지만 관리하기 때문이다. 또한, file mode 가 `160000`으로 나오는 것을 확이할 수 있는데, 이는 일반적인 파일이나 디렉터리가 아니라는 의미이다.

즉, 실제 작업 디렉터리(Working directory)에는 `theme/yourtheme`라는 이름의 디렉터리가 있고, 그 안에 또 하나의 Git 저장소가 있다. 하지만 슈퍼프로젝트의 관점에서는 `theme/yourtheme`는 서브모듈이기 때문에 참조하는 값만 관리하는 것이다.

서브모듈을 추가하면 서브모듈 내에서 해당 프로젝트의 내용을 수정하고 커밋(commit)이나 푸시(push) 할 수도 있다. 즉, 서브모듈도 일반적인 다른 저장소와 똑같이 사용할 수 있다. 그리고 이렇게 서브모둘을 수정하면 수정된 서브모듈의 커밋 해시(commit hash)가 새롭게 슈퍼프로젝트에 저장된다. 따라서 슈퍼프로젝트도 커밋해주어야 이 변경된 참조가 저장된다.

## 서브모듈을 가진 저장소를 클론(clone)하기

서브모듈을 사용하는 프로젝트를 Clone하면 해당 서브모듈 디렉토리는 빈 디렉터리다. 이떄는 먼저 `git submodule init` 명령으로 서브모듈을 초기화하고, `git submodule update` 명령으로 서브모듈 저장소를 가져와야 한다. 이 때 슈퍼프로젝트에 저장된 커밋 해시값을 참고하여 각 서브모듈들을 체크아웃(checkout)한다.

```bash
$ git submodule init
Submodule 'theme/yourtheme' (https://github.com/imjang57/yourtheme.git) registered for path 'theme/yourtheme'
$ git submodule update
Cloning into '/home/imjang57/mysite/themes/yourtheme'...
Submodule path 'themes/yourtheme': checked out '08d709f78b8c5b0fbeb7821e37fa53e69afcf433'
```

## Submodule Update

서브모듈을 최신 버전으로 업데이트하려면 서브모듈 디렉터리에서 `git fetch` 명령을 실행하고 `git merge` 명령으로 머지한다.

이후 메인 프로젝트(슈퍼프로젝트)에서 `git diff --submodule` 명령을 실행하면 업데이트된 서브모듈과 각 서브모듈에 추가된 커밋을 볼 수 있다. 이 상태에서 메인 프로젝트에서 `git commit` 명령으로 커밋하면 변경된 서브모듈 내용(커밋 해시)이 메인 프로젝트에 적용된다.

간단하게 이 작업을 하려면 `git submodule update --remote` 명령을 실행한다. 이 명령을 실행하면 Git이 스스로 서브모듈을 Fetch하고 업데이트한다. 이 명령을 기본적으로 `master` 브랜치를 체크아웃하고 업데이트를 수행한다. 브랜치를 바꾸려면 `.gitmodules` 파일을 다음과 같이 수정한다.

```
[submodule "theme/yourtheme"]
    path = theme/yourtheme
    url = https://github.com/imjang57/yourtheme
    branch = stable
```

# References

- https://git-scm.com/book/en/v2/Git-Tools-Submodules
- https://git-scm.com/book/ko/v2/Git-도구-서브모듈
