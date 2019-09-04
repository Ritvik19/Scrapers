# Lord-Varys

_The Master of Whisperers_

> My little birds are everywhere, and they whisper to me the strangest stories...

Web Scrapers for various websites

Dependencies:
* Anaconda Distribution for Python
* Scrapy Library
```pip install scrapy```
* PRAW
```pip intall praw```
* Selenium
```pip install selenium```
* Pdfkit (For saving Webpages as pdf)
```pip install pdfkit```

This repo consists of notebooks, scripts for automated browsers and crawlers that scrape:
* [Books2Scrape](https://books.toscrape.com) ```Crawler```
* [Quotes2Scrape](https://quotes.toscrape.com) ```Crawler```
* [TutorialsPoint](https://www.tutorialspoint.com/programming_examples/) ```Crawler```
* [Cambridge Dictionary](https://dictionary.cambridge.org/dictionary/): scrapes the defintion of word
* [CSS Tricks](https://css-tricks.com/snippets/)
* [Crazy Programmer](https://www.thecrazyprogrammer.com)
* [Cricbuzz](https://www.cricbuzz.com): live cricet scores
* [GitHub Profile Heatmap](https://github.com/Ritvik19/): scrapes the heatmap of any github profile
* [Google Images Scrapper](https://www.google.com/imghp?hl=en) ```Automated Browser``` 
* Image Crawler: Downloads all images from a webpage
* [IncludeHelp code-snippets](https://www.includehelp.com/code-snippets/)
* [Inshorts](https://inshorts.com/en/read)
* [Java](https://jaxenter.com/15-useful-code-snippets-java-developers-131796.html)
* [Jonas John](http://www.jonasjohn.de/snippets/all.htm)
* [jQuery](https://www.thecrazyprogrammer.com/2015/01/useful-jquery-code-snippets.html)
* [Medium-collections](https://medium.com/collections)
* [NASA APOD](https://api.nasa.gov/): Astronomy Picture of the Day ```API```
* OnThisDay: crawls through [On This Day](https://www.onthisday.com/) and [Britannica](https://www.britannica.com/on-this-day) to fetch data into json format
* [Project Euler](https://projecteuler.net/archives)
* [ProjectGutenberg](https://www.gutenberg.org/)
* [Python Snyppets](https://snippets.readthedocs.io/en/latest/)
* [Quotes2Scrape-Scroll](http://quotes.toscrape.com/scroll) ```Automated Browser```
* [Reddit-answers](https://www.reddit.com/r/answers/)
* [Reddit-Ask Me Anything](https://www.reddit.com/r/AMA/)
* [Reddit-Ask Reddit](https://www.reddit.com/r/AskReddit/)
* [Reddit-Ask Science](https://www.reddit.com/r/askscience/)
* [Reddit-Explain Like I'm Five](https://www.reddit.com/r/explainlikeimfive/)
* [Reddit-Life Pro Tips](https://www.reddit.com/r/LifeProTips/)
* [Reddit-Shower Thoughts](https://www.reddit.com/r/Showerthoughts/)
* [Reddit-Today I Learned](https://www.reddit.com/r/todayilearned/)
* [Reddit-wikipedia](https://www.reddit.com/r/wikipedia/)
* [Seb Sauvage](https://sebsauvage.net/python/snyppets/)
* [Snipplr](https://snipplr.com/popular/language)
* [Stackoverflow](https://stackoverflow.com): scrapes the result for a query
* [Syntax DB](https://syntaxdb.com/reference)
* [Weather](https://openweathermap.org/) : provides current weather info or 5 day forecast for a city ```API```
* Website Info: provides various info about a website using [Alexa](https://www.alexa.com/siteinfo/) and [Whois](https://www.whois.com/)

Instructions:
* Crawlers:
      Traverse to the directory in the command line and type
```scrapy crawl <crawler name> -o <outfilename>```
* Notebooks:
      Just run them in any jupyter environment
* Automated Browser:
    Make sure you have got chrome driver installed from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) before running the notebook
