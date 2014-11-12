leomeloxp.github.io
===================
# Introduction

This settings and README are heavily inspired on Spring.io's approach to keeping layout consistent between github pages.

The reason I'm making my own version is so that I can use my own layout and approach, as they seem to use tools which I don't yet use or need.

This repository was initially forked from theirs, so feel free to check them out as their original repo is pretty awesome.

Like Spring, my project pages are based on
[Jekyll](http://jekyllrb.com) and [GitHub Pages](http://pages.github.com/). This means that each project's website is stored within the project repo, in a special branch called "gh-pages".

# How to start a new `gh-pages` project page
### Create and checkout the gh-pages branch

    git checkout --orphan gh-pages

### Remove all files

    git rm -rf `git ls-files` && rm -rf *

### Add the gh-pages-upstream remote

    git remote add gh-pages-upstream https://github.com/leomeloxp/gh-pages.git

### Pull in the common site infrastructure

    git pull gh-pages-upstream gh-pages

## Edit `_config.yml`

Most of the settings in the _config.yml file are a default to all pages. Look for the Individual project section settings and change those according to your needs.

## Create the project home page
## Edit the content of your home page

### Edit the YAML front matter

## Commit your changes

    git commit -m "Initialize project page"
    git push --set-upstream origin gh-pages
    git push

# How to keep common gh-pages content up to date

> This assumes you've got the `gh-pages-upstream` remote set up, per the instructions in sections
above.

    git checkout gh-pages
    git pull --no-ff gh-pages-upstream gh-pages