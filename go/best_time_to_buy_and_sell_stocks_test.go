package algos

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestBest_Time_To_Buy_And_Sell_Stocks(t *testing.T) {
	assert.Equal(t, 5, bestTimeToBuyAndSellStocks([]int{7, 1, 5, 3, 6, 4}))
	assert.Equal(t, 0, bestTimeToBuyAndSellStocks([]int{7, 6, 4, 3, 1}))
}
