Title: Git Basics
Date: 2017-01-05
Modified: 2017-01-05
Tags: git
Slug: git-basics
Authors: imjang57
Summary: Git 기본 사용법

# Git Basic

이 글은 Git 에 대해 기본적인 내용은 알고 있다고 생각하고 정리 목적으로 작성된 글이니 Git 을 아예 모르면 [Git Book](http://git-scm.com/book/) 을 먼저 숙지하자.

아래 내용들에 알면 Git 을 잘 사용하기 위한 개념들은 다 알고 있다고 봐도 된다.

- VCS (Version Control System), DVCS (Distributed Version Control System)
- Working tree, Staging Area (Index), Local Repository, Remote Repository, Bare Repository

주로 아래 명령들이 사용된다.

- add, rm, mv, commit, push, pull, merge, diff, stash, rebase, fast-forward, history

# Git configuration

_Git_ 설정을 적용하는 방법은 2가지가 있다.

- `git config` command 를 사용하는 방법
- `.gitconfig` 파일에 추가하는 방법

`git config` 명령을 사용하면 git 프로그램이 자동으로 `.gitconfig` 파일에 해당 설정을 추가하는 것이기 때문에 결과는 같다.

`git config` command:

```bash
git config --global user.name "imjang57"
git config --global user.email "imjang57@gmail.com"
git config --global color.ui auto
```

git config file (`~/.gitconfig`):

```
[user]
    name = imjang57
    email = imjang57@gmail.com
[color]
    ui = auto
```

위에서 `git config --global` 과 같이 global option 을 전달했기 때문에 `~/.gitconfig` 파일에 설정이 저장되었다. 만약 특정 Git repository 에만 설정을 적용하고 싶으면 해당 Local git repository 로 가서 `git config --local` 과 같이 local option 을 사용하면 된다. 그러면 `<PROJECT_HOME>/.git/config` 에 설정이 저장된다.

--------------------------------------------------------------------------------

아래 설정은 git 이 실행할 텍스트 에디터 명령을 지정한다. commit message 작성 등을 위해 사용된다.

```
git config --global core.editor "\"C:\Windows\notepad.exe\""
git config --global core.editor "nano"
```

--------------------------------------------------------------------------------

아래 설정은 proxy 를 설정한다.

```bash
git config --global http.proxy http://<username>:<password>@<host>:<port>
git config --global https.proxy http://<username>:<password>@<host>:<port>
```

--------------------------------------------------------------------------------

아래 설정은 git 에서 사용하는 scheme 을 강제로 변환하기 위해 사용된다. 아래와 같이 설정하면 git scheme 을 https 로 바꿔서 사용하게 된다.

```bash
git config --global url."https://".insteadOf git://
```

# Git basic usage

## Git Local Repository 생성

- 새로운 git repository 생성 : `git init`

명령어를 실행한 경로에 `.git` 이라는 디렉터리가 생성되어 repository 관리 정보가 저장된다. `git init` 명령을 실행한 디렉터리의 내용을 _Working Tree_ 라고 한다. working tree 의 변경 내용이 있을 때 `git add`, `git rm` 등을 실행하면 _Index_ 가 생성된다. `git commit` 을 실행하면 local branch 에 변경 내용이 적용된다. `git push` 를 실행하면 remote branch 에 변경된 내용을 추가한다.

- Remote Repository 추가 : `git remote add <remote repository name> <Remote Repository URL>`

`git init` 후에 `git remote add` 를 통해 remote repoistory 를 추가할 수 있다. 이후 `git fetch` 을 실행하면 remote repository 의 정보를 읽어서 local repository 에 동기화한다. 그런데 `git fetch`는 working tree 에 이 정보들을 적용하지는 않는다. 단지 local repository 에만 정보를 저장한다. `git remote add origin ssh://user@host:22/repos/project` 로 remote repository 를 등록했으면 `git merge origin/master` 를 실행해서 merge 해야만 working tree 에 최신 정보가 적용된다. 만약 이 과정이 귀찮으면 그냥 `git pull` 을 실행하면 된다. `git pull` 은 `git fetch` 와 `git merge` 를 한꺼번에 실행해준다.

--------------------------------------------------------------------------------

Git Local Repository 를 만드는 다른 방법은 Remote Repository 를 복사하는 것이다. `git clone <url> [target directory]` 을 실행하면 remote repository 를 복사한다. target directory 를 지정해주지 않으면 remote repository 의 이름으로 target directory 가 생성된다.

--------------------------------------------------------------------------------

- remote repository 목록 확인 : `git remote`
- URL 포함하여 remote repository 목록 확인 : `git remote -v`
- remote repository 상세 정보 확인 : `git remote show [remote repository name]`

--------------------------------------------------------------------------------

- remote repository 를 삭제 : `git remote rm <remote repository name>`
- remote repository 의 이름 변경 : `git remote rename <from_name> <to_name>`

## Managing Modifications in local repository

Git 으로 변경사항들을 관리하기 위한 기본적인 명령들을에는 status, add, rm, mv, commit, stash, diff 등이 있다.

--------------------------------------------------------------------------------

- repository 상태 (현재 branch, 변경 내역 등) 확인 : `git status`

--------------------------------------------------------------------------------

- staging area (index) 에 파일 추가 : `git add <file>`

새롭게 생성된 Untracked files 나 modificated files 는 `git commit` 전에 `git add` 로 staging area 에 등록해야 한다. staging area 는 commit 전에 존재하는 임시 영역이다.

--------------------------------------------------------------------------------

- git repository 에 변경 내용을 기록 : `git commit [-m "messages"]`

Staging area 에 기록된 파일들을 실제 repository 에 반영하는 작업이다. -m 옵션이 없다면 git 환경설정에서 지정된 editor 가 실행되고 자세한 로그를 작성할 수 있다. 관례적으로 첫 번째 줄에는 로그에 대한 한 줄 요약을 작성하고 두 번째 줄은 공백, 세 번째 줄부터 상세 내용을 작성한다. 아무것도 입력하지 않고 editor 를 종료하면 commit 이 취소된다.

--------------------------------------------------------------------------------

- working tree 와 staging area 의 차이를 확인 : `git diff`
- staging area 와 laest commit 의 차이를 확인 : `git diff --staged`
- working tree 와 최신 commit 의 차이를 확인 : `git diff HEAD`
- 특정 branch 와 master branch 간의 diff 확인 : `git diff master..<branch name> [path]`

--------------------------------------------------------------------------------

- staging area 의 파일 삭제 : `git rm <path/to>`
- 특정 파일을 staging area 에서 삭제하지만 working tree 에는 보존 : `git rm --cached <path/to>`

--------------------------------------------------------------------------------

- 파일 이동 : `git mv <from_file> <to_file>`

--------------------------------------------------------------------------------

- 현재의 모든 변경 내용을 임시 저장하기 : `git stash`
- 가장 최근의 임시 저장된 내용을 다시 적용하기 : `git stash pop`
- 현재 임시 저장된 목록을 출력 : `git stash list`
- 가장 최근의 임시 저장된 내용을 삭제 : `git stash drop`

## Igrnoring files

`.gitigrnore` 파일에 무시할 파일들의 리스트를 추가하면 이후 추가된 파일들은 git add 등으로 변경 내용을 index 에 적용할 때 무시된다. 디렉터리마다 `.gitignore` 파일을 생성할 수 있으며 해당 디렉터리부터 하위 디렉터리 들에 대해 파일의 내용이 적용된다.

```
*.[oa]       # ignore files ending in ".o" or ".a"
!lib.a       # do track lib.a, even though you're ignoring .a files above
*~           # ignore files ending in tilde("~")
/TODO        # only ignore the root TODO file, not subdir/TODO
build/       # ignore all files in the build/ directory
doc/*.txt    # ignore doc/notes.txt, but not doc/server/arch.txt
doc/**/*.txt # ignore all "*.txt" files in the doc/ directory
```

`.gitignore` 파일의 다른 용도는 empty directory 를 repository 에 저장하기 위해 사용된다. git 은 빈 디렉터리는 저장소에 저장하지 않는다. 이때 빈 디렉터리 안에 임의의 빈 `.gitignore` 파일을 생성하여 commit 하면 해당 디렉터리도 저장소에 추가할 수 있다.

## Viewing the Commit History

- commit history 확인 : `git log [/path/to]`
- commit 에서 변경된 내용도 같이 확인 : - `git log -p [/path/to]`
- 마지막 2개의 내용만 확인 : `git log -2`
- 한줄 요약으로 보기 : `git log --pretty=oneline`

특정 파일의 version history list 를 확인하려면 `git log --follow [file]` 를 실행한다. git 나름대로 rename 한 작업까지 계산해준다.

## Working with Remote Repository

`git pull`, `git fetch`, `git merge`, `git push` 를 통해 remote repository 와 동기화할 수 있다.

--------------------------------------------------------------------------------

- Remote Repository 의 변경 내용들을 Local Repository 로 갱신 : `git pull`

원격 저장소의 변경 내용이 로컬 작업 디렉토리에 받아지고(fetch), 병합(merge)된다. `git pull` 은 내부적으로 아래의 두 명령이 연속적으로 실행된 것과 같다.

- `git fetch <remote repository name>`
- `git merge <remote repository name>/master`

--------------------------------------------------------------------------------

- Local Repository 의 commit 들을 Remote Repository 에 전달 : `git push [remote repository] [remote branch]`

Remote Repository 이름이 origin 이고, origin 의 master branch 로 Local Repository 의 변경 내용을 올리려고 하면 `git push origin master` 를 실행한다.

## Branch and Merge

- branch 목록 출력 및 현재 작업 중인 branch 확인 : `git branch`
- Remote Repository 의 branch 들을 모두 포함하여 출력 : `git branch -a`
- branch 생성 : `git branch <branch name>`
- branch 변경 : `git checkout <branch name>`
- branch 생성 및 변경 : `git checkout -b <branch name>`

만약 feature-A 라는 이름의 branch를 생성하고 해당 branch 로 변경하고 싶으면 `git checkout -b feature-A` 을 실행한다. 이는 다음 명령어 들을 연속으로 실행한 것과 같다.

- `git branch feature-A`
- `git checkout feature-A`

이후 master branch 로 돌아오려면 `git checkout master` 를 실행한다. 만약 현재 branch 를 사용하기 전의 branch 로 되돌아가려면 `git checkout -` 를 실행하면 된다.

- branch 삭제 : `git branch -d <branch name>`

--------------------------------------------------------------------------------

- branch 를 merge 하기 : `git merge [options] <branch name>`

만약 구현이 완료된 feature-A branch 를 merge 하려면 `git merge feature-A` 를 실행한다.

## Resolve conflicts

`git pull`, `git merge` 등을 하다보면 내가 변경하고 commit 한 내용과 다른 사람이 변경하고 commit 한 내용이 서로 충돌하는 경우가 발생한다. 대부분의 경우 git 이 자동으로 바뀐 부분을 알아서 적용해준다. 하지만 만약 서로 다른 사람들이 파일의 같은 부분을 동시에 고쳤을 경우, git 이 해결하지 못하고 충돌이 발생했음을 알려준다.

이렇게 충돌이 발생하면, git이 알려주는 파일의 충돌 부분을 직접 수정해서 병합이 가능하도록 수정해야 한다. 충돌을 해결했다면, `git add [file path]` 를 실행하여 수정된 부분을 다시 index 에 저장하고 commit 한다.

변경 내용을 병합하기 전에, `git diff` 를 사용하여 어떻게 바뀌었는지 비교해보는 것이 좋다.

## Tag

- Tag 목록 확인 : `git tag`
- Tag 생성 : `git tag <tag name>`
- Tag 삭제 : `git tag -d <tag name>`
- pattern 으로 tag 목록 확인 : `git tag -l 'v1.8.5*'`
- 특정 tag의 정보 보기 : `git show <tag name>`
- 이미 지나간 commit 에 대한 tag 를 생성 : git tag -a <tag name> <commit ID>
- remote server 에 tag 정보 push : `git push origin [tagname]`
- remote server 에 모든 tag 정보를 한꺼번에 전송 : `git push origin --tags`

git tag 에는 2가지 type 이 있다:

- lightweight : pointer to a specific commit. 즉, lightweight tag 정보는 오직 commit checksum 만 저장된다.
- annotated tag: stored as full objects in the Git database. They are checksummed; contain the tagger name, e-mail, and date; have a tagging message; and can be signed and verified with GNU Privacy Guard (GPG).

`git tag <tag name>` 으로 Tag 를 생성할 경우 기본적으로 libweight tag 이다. annotated tag 는 `-a` 옵션을 사용(`git tag -a <tag name> -m '<message>'`)해야 한다. `-m` 옵션이 없으면 git 에 editor 를 실행하여 message를 입력할 수 있도록 한다.

annotated tag 는 추가적인 tag 정보들(tag name, tagger, date, message 등)과 commit 내용을 보여 준다. lightweight tag 는 tag 관련된 추가적인 정보들이 없이 commit 내용만 보여준다.

- tag 로 checkout : `git checkout -b version2 v2.0.0`

git 에는 사실 tag 로 checkout 하는 기능은 없다. 단지 특정 tag 로 branch 를 만드는 것이다. 때문에 이렇게 만들어진 branch 에서 작업하고 commit 하면 master 에 반영이 안되니 주의해야 한다.

# Advanced

## Undo modifications

- Local 의 변경 내용을 HEAD 로 되돌리기: `git checkout -- <file path>`

위의 명령은 이미 인덱스에 추가된 변경 내용과 새로 생성한 파일은 그대로 남는다.

- Staging Area (index) 의 파일을 Unstaged 로 바꾸기: `git reset HEAD <file path>`

만약 어떤 파일을 수정한 후 git add 를 실행하여 Staged 상태일 때, 변경 내용들을 취소하고 싶을 경우 아래 명령들을 차례로 실행한다.

HEAD 는 Git 에서 사용되는 special pointer 이다. HEAD 는 현재 작업 중인 local branch 를 가리킨다. `git checkout` 으로 branch 를 변경하면 HEAD 가 변경된다.

- Repository 의 history 중 하나로 복원하기: `git reset [options] <commit hash ID>`
- history 와 모든 변경 내용들을 삭제하면서 특정 commit 으로 되돌아가기 : `git reset --hard [commit]`

`git reset --hard` 의 경우 history 를 포함한 모든 변경 내용들을 삭제하여 깔끔하게 이전 내용으로 되돌아갈 수 있다. 하지만 Local Git Repository 가 다른 Remote Repository 와 공유될 경우 문제가 발생할 수도 있다. 이때 사용가능 한 것이 `git revert <commit hash ID>` 이다. `git revert` 는 history 와 commit 들을 삭제하지 않는다. 내용을 특정 commit 으로 되돌리지만 삭제하지 않고 또하나의 새로운 commit 으로 처리한다.

## Modify commits

- commit 수정하기: `git commit --amend`

아래와 같은 경우 commit 내용을 수정해야 한다.

- 어떤 파일을 빼먹었을 때
- commit message 를 잘못 적었을 때

커밋을 했는데 Stage하는 것을 깜빡하고 빠트린 파일이 있으면 아래와 같이 고칠 수 있다:

```
git commit -m 'initial commit'
git add <forgotten_file_path>
git commit --amend
```

여기서 실행한 명령어 3개는 모두 하나의 commit 으로 기록된다. 두 번째 commit 은 첫 번째 commit 을 덮어쓴다.

# Github

- branch 들 (example: ruby on rails repository 의 4-0-stable branch 와 3-2-stable branch) 사이의 변경 내역 확인하는 방법 : `https://github.com/rails/rails/compare/4-0-stable...3-2-stable`
- master branch 의 2015년 1월 1일부터의 변경 내역을 확인하는 방법(변경 내역이 너무 많거나, 기간이 너무 긴 경우에는 최근 변경 내용만 나온다) : `https://www.github.com/rails/rails/compare/master@{2015-01-01}...master`

# References

- [Git Book English](http://git-scm.com/book/en/v2)
- [Git Book Korean](http://git-scm.com/book/ko/v2)
- [git - 간편 안내서](https://rogerdudler.github.io/git-guide/index.ko.html)

