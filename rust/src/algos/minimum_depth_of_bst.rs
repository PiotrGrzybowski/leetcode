use std::cell::RefCell;
use std::cmp::min;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub fn minimum_depth_of_bst(node: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    match node {
        Some(node) => match (node.borrow().left.clone(), node.borrow().right.clone()) {
            (Some(left), Some(right)) => {
                1 + min(
                    minimum_depth_of_bst(node.borrow().left.clone()),
                    minimum_depth_of_bst(node.borrow().right.clone()),
                )
            }
            (Some(left), None) => 1 + minimum_depth_of_bst(node.borrow().left.clone()),
            (None, Some(right)) => 1 + minimum_depth_of_bst(node.borrow().right.clone()),
            (None, None) => 1,
        },
        None => 0,
    }
}
