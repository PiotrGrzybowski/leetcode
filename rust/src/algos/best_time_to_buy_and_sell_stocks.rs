use std::cmp::{max, min};

pub fn best_time_to_buy_and_sell_stocks(prices: Vec<i32>) -> i32 {
    let mut profit = 0;
    let mut minimum = i32::MAX;
    for price in prices.iter() {
        minimum = min(minimum, *price);
        profit = max(profit, price - minimum);
    }
    profit
}
