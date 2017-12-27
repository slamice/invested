Detector:
- Save all stocks
- Get stocks with high volatility


Stock insights:
- Show stocks with high volatility
- Calculate average for each stock

Buy
- If stock is *buyable (lower by average, user_account.available_cash - stock > user_account.limit) then buy.
- Do only 3 times within 24 hours


Sell
- If stock is *sellable (higher by average) then sell.
- Do only 3 times within 24 hours













Algorithm
- Cycle through each stock, check average
- If stock