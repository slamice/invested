from Robinhood import Robinhood 

my_trader = Robinhood()
logged_in = my_trader.login(username="slamice", password="!")
stock_instrument = my_trader.instruments("GEVO")[0]
quote_info = my_trader.quote_data("GEVO")
print(quote_info)