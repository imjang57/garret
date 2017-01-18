Title: Windows 에서 Filename too long 에러
Date: 2017-01-18
Modified: 2017-01-18
Tags: windows, error
Slug: windows-error-filename-too-long
Authors: imjang57
Summary: Windows 에서 Filename too long 에러가 발생한 경우

# Windows 에서 Filename too long 에러

Windows 에서 Git 사용하다가 아래와 같은 에러가 발생했다.

```
fatal: cannot create directory at 'node_modules/gulp-clean/node_modules/gulp-util/node_modules/dateformat/node_modules/meow/node_modules/normalize-package-data/node_modules/validate-npm-package-license/node_modules/spdx-correct/node_modules/spdx-license-ids': Filename too long
warning: Clone succeeded, but checkout failed.
You can inspect what was checked out with 'git status'
and retry the checkout with 'git checkout -f HEAD'
```

에러 메시지 부분에 파일 이름이 매우 길고 메시지 끝에 `Filename too long` 이라는 글자가 보인다. 말그대로 파일 이름이 너무 길어서 나는 에러다.

[Stack Overflow](http://stackoverflow.com/questions/22575662/filename-too-long-in-git-for-windows/22575737#22575737)의 답변에 따르면 윈도우의 오래된 파일 API 를 사용하는 경우 파일 이름의 길이가 260글자까지만 가능하다. 최신 API 를 사용하면 4096글자까지 가능하다. Window 의 Git 이 사용하는 MinGW 가 오래된 API 를 사용하는 듯하다.

나는 Windows 7 에서 Git 1.9.x 버전을 사용하다가 위 에러를 만났다. 혹시나 해서 현재 최신 버전인 2.10.1 으로 다시 설치해봤지만 여전히 에러가 발생한다. 즉, 아직 고쳐지지 않았다는 이야기..

[같은 StackOverflow 질문에 달린 답변](http://stackoverflow.com/questions/22575662/filename-too-long-in-git-for-windows/26111092#26111092)에 따르면 아래 설정을 하면 된다고 한다.

```
git config --system core.longpaths true
```

하지만 위 설정을 해도 안된다. 위 설정으로 해결된다는 사람도 있는데 내 경우와 다른 점이 무엇인지 잘 모르겠다. 그래서 그냥 리눅스에 clone 한 Git repository 에서 export 해서 zip 으로 압축해서 옮겨왔다. 시간이 많지 않고, 다른 Git client 찾아서 설치하고 테스트하기도 귀찮고 윈도우에서 작업할게 아니라 테스트용이라..

[이 글](https://github.com/msysgit/msysgit/wiki/Git-cannot-create-a-file-or-directory-with-a-long-path)에 Git 이 윈도우에서 260자 제한을 건 기술적인 이유가 잘 나와있으니 궁금하면 읽어보자.

참고로, zip 파일을 윈도우에서 압축해제 할 때도 위 에러가 발생했다. 내가 사용하던 반디집(Bandizip) 프로그램이 예전 버전이라 오래된 API 를 사용하고 있었나 싶어서 최신으로 업데이트했다. 그러니 매우 잘 동작했다.

