def maxProfit(self, prices):
    sell, prev_sell, buy = 0, 0, prices[0]

    for price in prices:
        prev_buy, buy = buy, min(price - prev_sell, buy)
        prev_sell, sell = sell, max(price - prev_buy, sell)

    return sell
