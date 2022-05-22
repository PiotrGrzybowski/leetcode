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

pub fn sorted_array_to_bst_ranged(
    nums: &Vec<i32>,
    left: usize,
    right: usize,
) -> Option<Rc<RefCell<TreeNode>>> {
    return if left > right {
        None
    } else if left == right {
        Option::from(Rc::new(RefCell::new(TreeNode {
            val: nums[left],
            left: None,
            right: None,
        })))
    } else if right - left == 1 {
        Option::from(Rc::new(RefCell::new(TreeNode {
            val: nums[right],
            left: Option::from(Rc::new(RefCell::new(TreeNode {
                val: nums[left],
                left: None,
                right: None,
            }))),
            right: None,
        })))
    } else if right - left == 2 {
        Option::from(Rc::new(RefCell::new(TreeNode {
            val: nums[left + 1],
            left: Option::from(Rc::new(RefCell::new(TreeNode {
                val: nums[left],
                left: None,
                right: None,
            }))),
            right: Option::from(Rc::new(RefCell::new(TreeNode {
                val: nums[right],
                left: None,
                right: None,
            }))),
        })))
    } else {
        let middle = left + (right - left) / 2;
        Option::from(Rc::new(RefCell::new(TreeNode {
            val: nums[middle],
            left: sorted_array_to_bst_ranged(nums, left, middle - 1),
            right: sorted_array_to_bst_ranged(nums, middle + 1, right),
        })))
    };
}

pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
    sorted_array_to_bst_ranged(&nums, 0, nums.len() - 1)
}
