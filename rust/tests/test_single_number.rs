use rust::algos::single_number::single_number;

#[test]
fn test_single_number() {
    assert_eq!(1, single_number(Vec::from([2, 2, 1])));
    assert_eq!(4, single_number(Vec::from([4, 1, 2, 1, 2])));
    assert_eq!(1, single_number(Vec::from([1])));
}
