use rust::algos::max_depth_bst::{max_depth_bst, max_depth_bst2, TreeNode};
use std::cell::RefCell;
use std::rc::Rc;

#[test]
fn test_max_depth_bst() {
    let left = Option::from(Rc::new(RefCell::new(TreeNode::new(4))));
    let right = Option::from(Rc::new(RefCell::new(TreeNode::new(10))));
    let tree = Option::from(Rc::new(RefCell::new(TreeNode {
        val: 8,
        left: left,
        right: right,
    })));

    assert_eq!(2, max_depth_bst2(tree));
}
