def best_time_to_buy_and_sell_stocks(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    else:
        buy = prices[0]
        max_profit = 0
        for price in prices[1:]:
            buy = min(buy, price)
            max_profit = max(max_profit, price - buy)

        return max_profit


if __name__ == '__main__':
    assert best_time_to_buy_and_sell_stocks([7, 1, 5, 3, 6, 4]) == 5
    assert best_time_to_buy_and_sell_stocks([7, 6, 4, 3, 1]) == 0
