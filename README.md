
# Website www.grokit.ca

This is the source files for the website [http://www.grokit.ca/](http://www.grokit.ca/).

It is built using Django and Google App Engine. In order to deploy you will have to download the GAE Python ASK and put inside the "/app" folder.

# TODO

## A

- Remove 'categories', just tag is enough.

## B

- Have a way to automatically link to github pages (just have a convention for URL in /cnt?)
- Make image / files nesting happen with an automatic name-space.
- Make the computer science thing a normal article + 301.
- http://www.grokit.ca/tag should return cloud of tags
  - Fix the tags list not showing up in proper style.

## Blogging Platform with .docx Files

(https://gist.github.com/vzvenyach/7278543)
unoconv -f html test.docx
pandoc -f html -t markdown -o test.md test.html

## Improving Tagging System

tag::<tag> inline may be better than keeping seperate metadata in the file.
On the procesing side the only thing to do is just remove the tags from the presented text.

Could make this a broader rule with <action>::<parameter(s)>, could use "::", or ":::" (whatever is rare enough so that it does not conflict with another notation).

Try to pick a notation that is intuitive, does not conflict and is extendable beyond tagging.

## Blogging Directly Markdown

marked.min.js







