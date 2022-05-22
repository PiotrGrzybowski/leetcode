use rust::algos::best_time_to_buy_and_sell_stocks::best_time_to_buy_and_sell_stocks;

#[test]
fn test_best_time_to_buy_and_sell_stocks() {
    assert_eq!(
        5,
        best_time_to_buy_and_sell_stocks(Vec::from([7, 1, 5, 3, 6, 4]))
    );
    assert_eq!(
        0,
        best_time_to_buy_and_sell_stocks(Vec::from([7, 6, 4, 3, 1]))
    );
}
