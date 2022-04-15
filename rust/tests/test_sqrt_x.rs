use rust::algos::sqrt_x::my_sqrt;

#[test]
fn test_add_binary() {
    assert_eq!(my_sqrt(0), 0);
    assert_eq!(my_sqrt(1), 1);
    assert_eq!(my_sqrt(3), 1);
    assert_eq!(my_sqrt(4), 2);
    assert_eq!(my_sqrt(8), 2);
    assert_eq!(my_sqrt(16), 4);
    assert_eq!(my_sqrt(2147395599), 46339);
}
