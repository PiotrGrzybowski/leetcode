use std::cell::RefCell;
use std::cmp::max;
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

pub fn max_depth_bst(tree: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    match tree {
        Some(node) => {
            1 + max(
                max_depth_bst(node.borrow().left.clone()),
                max_depth_bst(node.borrow().right.clone()),
            )
        }
        None => 0,
    }
}
