# CRYPTO_BOT
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python-based cryptocurrency data fetcher from Yobit API.

## Description
CRYPTO_BOT is a Python script for fetching and analyzing cryptocurrency data from Yobit API. 
It supports operations like fetching trading pairs, market depth, recent trades, and more.


## Getting Started

### Installation 
1. Clone the repository:
```
https://github.com/YuryHerasimau/crypto_bot.git
```
2. Install dependencies:
```
pip install -r requirements.txt
``` 

### Usage
To run, use command line arguments:
```
python main.py --mode trades --base btc --limit 1000
```

## Features
- Fetch info about all trading pairs.
- Analyze market depth and calculate bid volume.
- View recent trades and summarize buy/sell statistics.
- Save data in JSON format.

## Technologies
- Python 3.8+
- Requests Library
- Yobit API

## Roadmap
- [x] Fetch cryptocurrency data.
- [ ] Add support for multiple APIs.