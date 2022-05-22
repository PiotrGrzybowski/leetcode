package algos

func bestTimeToBuyAndSellStocks(prices []int) int {
	if len(prices) < 2 {
		return 0
	} else {
		buy := prices[0]
		maxProfit := 0

		for i := 1; i < len(prices); i++ {
			buy = min(buy, prices[i])
			maxProfit = max(maxProfit, prices[i]-buy)
		}
		return maxProfit
	}
}
