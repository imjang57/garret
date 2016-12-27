Title: Hello, site
Date: 2016-12-26 20:30
Modified: 2016-12-26 20:30
Slug: hello-site
Authors: imjang57
Summary: First post.

# Hello, site

This is first post of this site.

Metadata syntax for markdown posts:

```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
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
ghp-import -m "Generate Pelican site" -b gh-pages /home/youngho/venv/garret/garret/output
```

Finally, push loca gh-pages branch to github gh-pages branch:

```
git checkout gh-pages
git push -u origin gh-pages
```