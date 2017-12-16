# garret

개인적으로 나중에 혹시나 쓸 일이 있을까 하는 것들을 적는 곳입니다. 사실 나중에 다시 찾기 귀찮아서.... 그러니까 글들이 불친절하게 작성되었습니다. 써놓고 까먹고 안올리고 있다가 한꺼번에 올리고 그러니까 날짜도 뒤죽박죽입니다. 대충 관리하니 주의깊게 보지 마세요.

# Download and Installation

```bash
$ git clone http://github.com/imjang57/garret
$ cd garret
$ git submodule init
$ git submodule update
```

# Publish

- To generate site : `pelican /path/to/content [-o /path/to/output] [-s publishconf.py]`
- To publish site to git gh-pages branch of local repository : `ghp-import -m "Generate Pelican site" -b gh-pages output`
- To deploy site to gh-pages of github : `git push origin gh-pages`

# Markdown

- [Github Basic writing and formatting syntax](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
- [Github Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [CommonMark](http://commonmark.org)
- [Python Markdown module](http://pythonhosted.org/Markdown/)
- [Online Markdown editor](http://jbt.github.io/markdown-editor)

# References

- [Pelican Home](http://blog.getpelican.com)
- [Pelican Github](https://github.com/getpelican/pelican)
- [Pelican Document](http://docs.getpelican.com)
