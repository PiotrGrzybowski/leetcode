use rust::algos::valid_parentheses::valid_parentheses;

#[test]
fn test_valid_parentheses() {
    assert_eq!(valid_parentheses(String::from("()")), true);
    assert_eq!(valid_parentheses(String::from("()[]{}")), true);
    assert_eq!(valid_parentheses(String::from("()]")), false);
}
