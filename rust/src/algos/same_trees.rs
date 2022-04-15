use std::cell::RefCell;
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

pub fn is_same_tree(
    first: Option<Rc<RefCell<TreeNode>>>,
    second: Option<Rc<RefCell<TreeNode>>>,
) -> bool {
    match (first, second) {
        (None, None) => true,
        (Some(_), None) => false,
        (None, Some(_)) => false,
        (Some(first), Some(second)) => {
            first.borrow().val == second.borrow().val
                && is_same_tree(first.borrow().left.clone(), second.borrow().left.clone())
                && is_same_tree(first.borrow().right.clone(), second.borrow().right.clone())
        }
    }
}
