use rust::algos::implement_str_str::str_str;

#[test]
fn test_two_sum() {
    assert_eq!(str_str(String::from("hello"), String::from("")), 0);
    assert_eq!(str_str(String::from("hello"), String::from("ll")), 2);
    assert_eq!(str_str(String::from("hello"), String::from("22e")), -1);
    assert_eq!(str_str(String::from("aaaa"), String::from("aaa")), 0);
    assert_eq!(str_str(String::from("aaa"), String::from("aaaa")), -1);
}
