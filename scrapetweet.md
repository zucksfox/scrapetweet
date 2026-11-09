# scrapetweet

Search recent tweets by keyword using the X API, with automatic retry on rate limits.

## How it works

`scrapetwet.py` uses [Tweepy](https://www.tweepy.org/) to call the X API v2 recent-search
endpoint. You enter a search query and how many tweets to fetch (10–100); matching tweets are
printed to the terminal. If the API rate limit is hit, the script backs off exponentially and
retries (up to 5 times).

## Requirements

- Python 3
- A [X Developer](https://developer.x.com/en/portal) Bearer Token

## Setup

```bash
pip install tweepy
```

Open `scrapetwet.py` and replace `'your_bearer_token'` with your own Bearer Token.

## Usage

```bash
python scrapetwet.py
```

Then enter your search query and the number of tweets to retrieve (10–100, default 10).

## Tech

- Python
- Tweepy (X API v2 client)
