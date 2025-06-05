import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

# Load .env config
load_dotenv(override=True)

ALPACA_API_KEY_ID= os.getenv("ALPCA_API_KEY_ID")
ALPACA_API_SECRET_KEY = os.getenv("ALPCA_API_SECRET_KEY")
ALPACA_API_BASE_URL = os.getenv("ALPCA_API_BASE_URL")


trading_client = TradingClient(ALPACA_API_KEY_ID, ALPACA_API_SECRET_KEY, paper=True)

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('{} account has ${} is available as buying power.'.format(account.id, account.buying_power))
