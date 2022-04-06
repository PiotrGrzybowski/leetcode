use rust::algos::palindrome_number::is_palindrome;

#[test]
fn test_two_sum() {
    assert_eq!(is_palindrome(121), true);
    assert_eq!(is_palindrome(-121), false);
    assert_eq!(is_palindrome(10), false);
    assert_eq!(is_palindrome(10099001), true);
}
