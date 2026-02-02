"""
This program, through the website, checks the version of the program and if the version has not changed,
It updates the necessary information.
You can test the program by activating the "test_IAP" function.
Set its parameter to "true" to test.
Also, the payment type must be Litecoin.
https://blockchair.com/litecoin/transaction/61a7667851da2d1395c26f4eaba7a14a3c1355ba80e1b35678327619a115d21e
"""
TESTING = False
PRICE_TEST_IS_OK = False
DATE_TEST_IS_OK = False
TIME_TEST_IS_OK = False
BUY_CLICKED = False

TOTAL_TIME = [1 * 60 + 1]
APP_PRICE = 0.01  # in US Dollar

the_coins = (
    "Bitcoin (BTC)",
    "Dogecoin (DOGE)",
    "Litecoin (LTC)",
    "Tron (TRX)"
)


other_vars = {
}

# Input data for verifying payment
registered_txid = ""
registered_address = ""
registered_clock = ""
registered_money = ""

