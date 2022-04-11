use rust::algos::length_of_last_word::length_of_last_word;

#[test]
fn test_two_sum() {
    assert_eq!(length_of_last_word(String::from("a")), 1);
    assert_eq!(length_of_last_word(String::from("Hello World")), 5);
    assert_eq!(length_of_last_word(String::from("luffy is still joyboy")), 6);
    assert_eq!(length_of_last_word(String::from("   fly me   to   the moon  ")), 4);
}
