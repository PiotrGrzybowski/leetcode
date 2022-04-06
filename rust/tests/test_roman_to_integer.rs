use rust::algos::roman_to_integer::roman_to_int;

#[test]
fn test_two_sum() {
    assert_eq!(roman_to_int(String::from("III")), 3);
    assert_eq!(roman_to_int(String::from("LVIII")), 58);
    assert_eq!(roman_to_int(String::from("MCMXCIV")), 1994);
}
