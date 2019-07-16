# Lord-Pyrys

_The Master of Whisperers_

> My little birds are everywhere, and they whisper to me the strangest stories...

Web Scraper for various websites

Just run any notebook to scrape the corresponding website,

dependencies:
* Anaconda Python Distribution
* Scrapy Library
```
pip install scrapy
```

This repo consists of notebooks and crawlers that scrape:
* [Books2Scrape](https://books.toscrape.com) Crawler: *books*
* [Quotes2Scrape](https://quotes.toscrape.com) Crawler: *quotes*
* [TutorialsPoint](https://www.tutorialspoint.com/programming_examples/) Crawler: *snippets*
* [CSS Tricks](https://css-tricks.com/snippets/)
* [Crazy Programmer](https://www.thecrazyprogrammer.com)
* Image Crawler: Downloads all images from a webpage
* [IncludeHelp code-snippets](https://www.includehelp.com/code-snippets/)
* [Inshorts](https://inshorts.com/en/read)
* [Java](https://jaxenter.com/15-useful-code-snippets-java-developers-131796.html)
* [Jonas John](http://www.jonasjohn.de/snippets/all.htm)
* [jQuery](https://www.thecrazyprogrammer.com/2015/01/useful-jquery-code-snippets.html)
* OnThisDay: crawls through [On This Day](https://www.onthisday.com/) and [Britannica](https://www.britannica.com/on-this-day) to fetch data into json format
* [Project Euler](https://projecteuler.net/archives)
* [Python Snyppets](https://snippets.readthedocs.io/en/latest/)
* [Reddit-Today I Learned](https://www.reddit.com/r/todayilearned/) : praw
```
pip intall praw
```
* [Seb Sauvage](https://sebsauvage.net/python/snyppets/)
* [Snipplr](https://snipplr.com/popular/language)
* [Syntax DB](https://syntaxdb.com/reference)
* [Weather](https://openweathermap.org/) : provides current weather info or 5 day forecast for a city
* Website Info: provides various info about a website using [Alexa](https://www.alexa.com/siteinfo/) and [Whois](https://www.whois.com/)

Instructions:
* Crawlers:
      Traverse to the directory in the command line and type
```
scrapy crawl <crawler name> -o <outfilename>
```
* Notebooks:
      Just run them in any jupyter environment
