use rust::algos::merge_sorted_arrays::merge;

#[test]
fn test_merge_sorted_arrays() {
    assert_eq!(
        merge(&mut vec![1, 2, 3, 0, 0, 0], 3, &mut vec![2, 5, 6], 3),
        vec![1, 2, 2, 3, 5, 6]
    );
    assert_eq!(
        merge(
            &mut vec![1, 2, 2, 3, 3, 4, 8, 0, 0, 0, 0, 0],
            7,
            &mut vec![2, 2, 3, 3, 5],
            5
        ),
        vec![1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 8]
    );
    assert_eq!(merge(&mut vec![1], 1, &mut vec![], 0), vec![1]);
    assert_eq!(merge(&mut vec![0], 0, &mut vec![1], 1), vec![1]);
}
