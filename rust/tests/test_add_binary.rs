use rust::algos::add_binary::add_binary;

#[test]
fn test_add_binary() {
    assert_eq!(add_binary(String::from("11"), String::from("1")), String::from("100"));
    assert_eq!(add_binary(String::from("1010"), String::from("1011")), String::from("10101"));
}