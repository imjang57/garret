Title: Hello, site
Date: 2016-12-26
Modified: 2016-12-26
Category: hello
Tags: hello, site 
Slug: hello-site
Authors: imjang57
Summary: My first post.

# Hello, site

This is first post of this site.

Metadata syntax for markdown posts:

```
Title: My super title
Date: 2010-12-03
Modified: 2010-12-05
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.
```

This site published by [pelican](http://blog.getpelican.com). Document is [here](http://docs.getpelican.com).

To generate site, run follow command:

```
pelican /path/to/content [-o /path/to/output] [-s publishconf.py]
```

To publish site to git gh-pages repository, run follow command:

```
ghp-import -m "Generate Pelican site" -b gh-pages output
```

Finally, push loca gh-pages branch to github gh-pages branch:

```
git checkout gh-pages
git push -u origin gh-pages
```

# References

- [Pelican Github](https://github.com/getpelican/pelican)
- [Pelican Home](http://blog.getpelican.com)
- [Pelican Document](http://docs.getpelican.com)

