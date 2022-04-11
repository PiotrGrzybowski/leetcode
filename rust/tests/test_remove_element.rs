use rust::algos::remove_element::remove_element;

#[test]
fn test_two_sum() {
    assert_eq!(remove_element(&mut vec![3,2,2,3], 3), 2);
    assert_eq!(remove_element(&mut vec![0,1,2,2,3,0,4,2], 2), 5);
}
