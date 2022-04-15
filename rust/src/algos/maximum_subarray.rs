use std::cmp::max;

pub fn max_sub_array(nums: Vec<i32>) -> i32 {
    let mut best: i32 = i32::MIN;
    let mut current_max = 0;

    for value in nums.iter() {
        current_max = max(*value, current_max + value);
        best = max(best, current_max);
    }
    best
}
