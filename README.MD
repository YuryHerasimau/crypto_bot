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

## Usage

### Public API
To use the public methods (fetching information about currency pairs, tickers, order depth, and trades), run the script with the corresponding `--mode` argument.

Examples:
```
python main.py --mode info
python main.py --mode ticker --base eth
python main.py --mode depth --base xrp --limit 100
python main.py --mode trades --base btc --limit 1000
```

### Private API
To use private API methods that require authentication through your API key and secret, use the `--private` flag and provide the required parameters, such as the coin name to fetch a deposit address.

Examples:
```
python main.py --private --mode private_info
python main.py --private --mode deposit_address --coin_name eth
```

### Arguments
* `--mode`: Defines the mode of operation. Options include:
    * `--info`: Fetch general info about available pairs on the exchange.
    * `--ticker`: Get information about a currency pair (e.g., `btc_usdt`).
    * `--depth`: Get the order book depth for a specific pair.
    * `--trades`: Get trade data for a specific pair.
    * `--private_info`: Fetch private information about balances and API privileges.
    * `--deposit_address`: Fetch a deposit address for a specific coin.
* `--base`: (Optional) The base currency (default is `btc`). Used for `ticker`, `depth`, `trades`, etc.
* `--limit`: (Optional) The limit for depth or trades (default is `150`).
* `--private`: (Optional) Flag to indicate that private API methods should be used.
* `--coin_name`: (Optional) The coin name (e.g., `btc`, `eth`) for methods like `deposit_address`.

## Environment Variables
For API keys and secrets, create a `.env` file with the following content:
```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
BASE_URL=https://yobit.net
PUBLIC_API_URL=/api/3
PRIVATE_API_URL=/tapi
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
- [x] Add support for private API and CLI options.
- [ ] Add support for multiple APIs.
- [ ] Improve error handling and logging.