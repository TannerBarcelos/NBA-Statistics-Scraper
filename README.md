# NBA-Statistics-Scraper

## About The Project

- Robust web scraper that scrapes NBA stats from [BasketballReference](https://www.basketball-reference.com/) and pipes that data into MySQL. This data is then used as the source of truth for the custom NBA Stats API [here](https://github.com/TannerBarcelos/NBA-Statistics-API)
- This serves as an ETL pipeline which will scrape the pages needed to then source the API being developed at the link above. This code will run on CRON job hosted on Heroku

- Team logos and player images will be hosted in an S3 bucket, the database will be hosted in an RDS instance and the scraper will run once a day through being served on AWS as well
