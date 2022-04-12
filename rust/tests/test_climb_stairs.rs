use rust::algos::climb_stairs::climb_stairs;

#[test]
fn test_climb_stairs() {
    assert_eq!(climb_stairs(2), 2);
    assert_eq!(climb_stairs(3), 3);
    assert_eq!(climb_stairs(8), 34);
    assert_eq!(climb_stairs(16), 1597);
}
