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

pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool {
    match root {
        Some(node) => match (node.borrow().left.clone(), node.borrow().right.clone()) {
            (None, None) => node.borrow().val == target_sum,
            _ => {
                path_sum(node.borrow().left.clone(), target_sum - node.borrow().val)
                    || path_sum(node.borrow().right.clone(), target_sum - node.borrow().val)
            }
        },
        None => false,
    }
}
