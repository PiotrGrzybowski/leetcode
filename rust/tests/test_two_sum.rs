use rust::algos::two_sum::two_sum;

#[test]
fn test_two_sum() {
    assert_eq!(two_sum(vec![0, 1, 4, 11, 2, 3, 11, 7], 9), vec![4, 7]);
    assert_eq!(two_sum(vec![3, 3], 6), vec![0, 1]);
    assert_eq!(two_sum(vec![3, 2, 4], 6), vec![1, 2]);
    assert_eq!(two_sum(vec![2, 0, 0, 0, 0, 11, 15, 7], 9), vec![0, 7]);
}
