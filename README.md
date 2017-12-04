# wiki_philosophy
```
Wiki Crawler
Starting from a random Wikipedia article (example: http://en.wikipedia.org/wiki/Art) and clicking
on the first non-italicized link not surrounded by parentheses in the main text and then repeating
the process for subsequent articles usually leads to http://en.wikipedia.org/wiki/Philosophy.
Please write a program that models this behavior and answers the following questions, while
making as few http requests as possible.

# Questions:
## What percentage of pages lead to philosophy?
## Using the random article link (found on any wikipedia article in the left sidebar),
   what is the distribution of path lengths for 500 pages, discarding those paths that never reach the Philosophy page?
```

## Dependencies

- python2
- BeautifulSoup

## Running Program:

Please from terminal run
`python wiki-crawler.py`

the result would be something like:
```
percentage of page lead to philosophy: 100.0%
random percentage of page lead to philosophy: 80.0%
Counter({15: 3, 10: 1, 13: 1})
```
