# Lord-Varys

_The Master of Whisperers_

> My little birds are everywhere, and they whisper to me the strangest stories...

Web Scrapers for various websites

Dependencies:
* Anaconda Distribution for Python
* Scrapy
* Scrapy-Selenium
* PRAW
* Selenium
* Pdfkit (For saving Webpages as pdf)
* Spotipy

This repo consists of chrome extensions,  notebooks, scripts for automated browsers and crawlers that scrape:
* [Youtube-Downloader](https://www.youtube.com): Downloads YouTube Videos ```Chrome Extension```
* Sherlock-Holmes: General Purpose Webpage scrapper ```Chrome Extension```

* [AltNews](https://www.altnews.in)
  
      scrapy crawl education
      scrapy crawl news
      scrapy crawl politics
      scrapy crawl religion
      scrapy crawl science
      scrapy crawl society

* [ANI](https://aninews.in/)
  
      scrapy crawl news

* [Books2Scrape](https://books.toscrape.com)
 
      scrapy crawl books

* [Cambridge Dictionary](https://dictionary.cambridge.org/dictionary/): scrapes the defintion of word

      scrapy crawl dict -a query=<query>

* [CodeChef](https://www.codechef.com/)
      
      scrapy crawl all
      scrapy crawl beginner
      scrapy crawl easy
      scrapy crawl medium
      scrapy crawl hard
      scrapy crawl challenge
      scrapy crawl peer

* [CodeForces](https://codeforces.com/)
      
      scrapy crawl problems

* [CodeGrepper](https://www.codegrepper.com/)

      scrapy crawl codesnippets

* Emails: Crawl emails mentioned on a complete website

      scrapy crawl emails -a start_url=<homepage_url> -a thresh=<num bw 1 & 100> -a restrict_domain=<0 or 1>

* [Github](https://github.com)
  
      scrapy crawl profileheatmap -a username=<username>

* [IMDB](https://www.imdb.com/chart/top)

      scrapy crawl best_movies

* [IndiaTV](https://www.indiatvnews.com/)

      scrapy crawl auto
      scrapy crawl brandcontent
      scrapy crawl business
      scrapy crawl crime
      scrapy crawl education
      scrapy crawl entertainment
      scrapy crawl fyi
      scrapy crawl health
      scrapy crawl india
      scrapy crawl jobs
      scrapy crawl lifestyle
      scrapy crawl politics
      scrapy crawl science
      scrapy crawl sports
      scrapy crawl technology
      scrapy crawl trending
      scrapy crawl world

* [Inshorts](https://inshorts.com/en/read)

      scrapy crawl automobile
      scrapy crawl business
      scrapy crawl entertainment
      scrapy crawl hatke
      scrapy crawl home
      scrapy crawl miscellaneous
      scrapy crawl national
      scrapy crawl politics
      scrapy crawl science
      scrapy crawl sports
      scrapy crawl sports
      scrapy crawl startup
      scrapy crawl technology
      scrapy crawl world

* [JantaKaReporter](http://www.jantakareporter.com/)

      scrapy crawl news

* [Keep Inspiring](https://www.keepinspiring.me/category/quotes/)

      scrapy crawl quotes

* [LiveCoin](https://www.livecoin.net/en)

      scrapy crawl livecoin

* [Medium Stats](https://medium.com/): Stats for the articles of various publications

      scrapy crawl analyticsvidhya -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl betterhuman -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl bettermarketing -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl betterprogramming -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl codeburst -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl dailyjs -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl datadriveninvestor -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl devbits -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl every30days -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl forge -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl freecodecamp -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl googledevelopers -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl javascriptinplainenglish -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl jupyterblog -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl learningnewstuff -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl levelupcoding -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl lifeofthought -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl omgfacts -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl onezero -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl pythonfeatures -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl pythoninplainenglish -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl pythonpandemonium -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl therenaissancedeveloper -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl thestartup -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl thewritingcooperative -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl towardsdatascience -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>
      scrapy crawl uxcollective -a sdate=<yyyy-mm-dd> -a edate=<yyyy-mm-dd>

* [MensXP](https://www.mensxp.com/)

      scrapy crawl culture
      scrapy crawl entertainment
      scrapy crawl fashion
      scrapy crawl grooming
      scrapy crawl relationships
      scrapy crawl social
      scrapy crawl sports
      scrapy crawl technology

* [NASA APOD](https://api.nasa.gov/)

      scrapy crawl apod

* [OneLineFun](https://onelinefun.com)

      scrapy crawl oneliners
      
* [OpIndia](https://www.opindia.com/)
      
      scrapy crawl opindia

      scrapy crawl crime
      scrapy crawl economy
      scrapy crawl entertainment
      scrapy crawl explainer
      scrapy crawl factcheck
      scrapy crawl government
      scrapy crawl law
      scrapy crawl media
      scrapy crawl opinions
      scrapy crawl politicalhistory
      scrapy crawl politics
      scrapy crawl sports
      scrapy crawl variety
      scrapy crawl virtualworld

* [PostcardNews](https://postcard.news/timeline)
      
      scrapy crawl timeline

* [ProjectEuler](https://projecteuler.net/archives)
      
      scrapy crawl problems

* [Pypi](https://pypi.org)
      
      scrapy crawl packagedependency -a package=<packagename>

* [Quotes2Scrape](https://quotes.toscrape.com)

      scrapy crawl quotes

* [Reddit](http://reddit.com/)

      scrapy crawl reddit -a subreddit=<subreddit-name>

* [RVCJ](http://rvcj.com/)

      scrapy crawl rvcj

* [ScoopWhoop](https://www.scoopwhoop.com/)

      scrapy crawl stories

* [Shine_com](https://shine.com/)

      scrapy crawl accounting-jobs
      scrapy crawl finance-accounts-investment-banking-jobs

* [SixWordStories](https://http://www.sixwordstories.net/)
      
      scrapy crawl stories

* [SlickDeals](https://slickdeals.net/deal-categories/)

      scrapy crawl computer

* [Swarajya](https://swarajyamag.com/)

      scrapy crawl api

* [Syntax DB](https://syntaxdb.com/reference)

      scrapy crawl snippets

* [TFIPost](https://tfipost.com/)

      scrapy crawl posts

* [TheWeek](https://www.theweek.in/home.html)

      scrapy crawl stories

* [TheWire](https://thewire.in/)

      scrapy crawl posts

* [They Said So](https://theysaidso.com/api/)

      scrapy crawl qod

* [TutorialsPoint](https://www.tutorialspoint.com/programming_examples/)

      scrapy crawl snippets

* [ViralNova](https://viralnova.com/)

      scrapy crawl viralnova

* [ViralStories](http://viralstories.in/)

      scrapy crawl viralstories

* [Weather](https://openweathermap.org/)

      scrapy crawl weather -a city=<city>
      scrapy crawl forecast -a city=<city>

* [Brainy Quote](https://www.brainyquote.com) ```Automated Browser```
* [CSS Tricks](https://css-tricks.com/snippets/)
* [Crazy Programmer](https://www.thecrazyprogrammer.com)
* [Cricbuzz](https://www.cricbuzz.com): live cricket scores
* EmailCrawler: Extract Email Address from a website
* [Goodreads-Quotes](https://www.goodreads.com/quotes)
* [Google Images Scrapper](https://www.google.com/imghp?hl=en) ```Automated Browser```
* Image Crawler: Downloads all images from a webpage
* [IncludeHelp code-snippets](https://www.includehelp.com/code-snippets/)
* [Java](https://jaxenter.com/15-useful-code-snippets-java-developers-131796.html)
* [Jonas John](http://www.jonasjohn.de/snippets/all.htm)
* [jQuery](https://www.thecrazyprogrammer.com/2015/01/useful-jquery-code-snippets.html)
* [Medium-collections](https://medium.com/collections)
* OnThisDay: crawls through [On This Day](https://www.onthisday.com/) and [Britannica](https://www.britannica.com/on-this-day) to fetch data into json format
* [ProjectGutenberg](https://www.gutenberg.org/)
* [Python Snyppets](https://snippets.readthedocs.io/en/latest/)
* [Quotes2Scrape-Scroll](http://quotes.toscrape.com/scroll) ```Automated Browser```
* [Seb Sauvage](https://sebsauvage.net/python/snyppets/)
* [Snipplr](https://snipplr.com/popular/language)
* [Spotify](https://www.spotify.com/in/) ```API```
* [Stackoverflow](https://stackoverflow.com): scrapes the result for a query
* Website Info: provides various info about a website using [Alexa](https://www.alexa.com/siteinfo/) and [Whois](https://www.whois.com/)

Instructions:
* Crawlers:
      Traverse to the directory in the command line and type
```scrapy crawl <crawler name> -o <outfilename>```
* Notebooks:
      Just run them in any jupyter environment
* Automated Browser:
    Make sure you have got chrome driver installed from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) before running the notebook
