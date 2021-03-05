# NBA-Statistics-Scraper

## About The Project
- Robust web scraper that scrapes NBA stats from [BasketballReference](https://www.basketball-reference.com/) and pipes that data into MySQL. This data is then used as the source of truth for the custom NBA Stats API [here](https://github.com/TannerBarcelos/NBA-Statistics-API)
- This serves as an ETL pipeline which will scrape the pages needed to then source the API being developed at the link above. This code will run on CRON job hosted on Heroku
