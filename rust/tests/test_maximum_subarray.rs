use rust::algos::maximum_subarray::max_sub_array;

#[test]
fn test_two_sum() {
    assert_eq!(max_sub_array(vec![-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6);
    assert_eq!(max_sub_array(vec![1]), 1);
    assert_eq!(max_sub_array(vec![5, 4, -1, 7, 8]), 23);
}
