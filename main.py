import argparse
from api.public_api import get_info, get_ticker, get_depth, get_trades
from api.private_api import get_private_info, get_deposit_address


def main():
    parser = argparse.ArgumentParser(
        description="Fetch cryptocurrency data from Yobit API."
    )
    parser.add_argument(
        "--mode",
        choices=[
            "info",
            "ticker",
            "depth",
            "trades",
            "private_info",
            "deposit_address",
        ],
        required=True,
        help="Mode of operation.",
    )
    parser.add_argument("--base", default="btc", help="Base currency (e.g., btc).")
    parser.add_argument(
        "--limit",
        type=int,
        default=150,
        help="Limit for depth or trades (default: 150).",
    )
    parser.add_argument(
        "--private", action="store_true", help="Use private API methods."
    )
    parser.add_argument(
        "--coin_name",
        default="btc",
        help="Coin name for deposit address (e.g., btc, eth).",
    )
    args = parser.parse_args()

    if args.private:
        if args.mode == "private_info":
            print(get_private_info())
        elif args.mode == "deposit_address":
            # coin_name = input("Enter a coin name: ")
            print(get_deposit_address(coin_name=args.coin_name))
        else:
            print("Invalid mode for private API")

    else:
        if args.mode == "info":
            print(get_info())
        elif args.mode == "ticker":
            print(get_ticker(base_currency=args.base))
        elif args.mode == "depth":
            print(get_depth(base_currency=args.base, limit=args.limit))
        elif args.mode == "trades":
            print(get_trades(base_currency=args.base, limit=args.limit))
        else:
            print("Invalid mode for public API")


if __name__ == "__main__":
    main()
