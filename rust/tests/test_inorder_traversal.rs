use rust::algos::inorder_traversal::inorder_traversal;

#[test]
fn test_inorder_traversal() {
    assert_eq!(inorder_traversal(1), vec![1, 3, 2]);
}
