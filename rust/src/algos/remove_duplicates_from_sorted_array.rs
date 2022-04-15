pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    let mut slow: usize = 0;
    let mut fast: usize = 1;

    while fast < nums.len() {
        while fast < nums.len() && nums[slow] == nums[fast] {
            fast += 1;
        }
        if fast < nums.len() {
            slow += 1;
            nums[slow] = nums[fast];
        }
    }
    (slow + 1) as i32
}
