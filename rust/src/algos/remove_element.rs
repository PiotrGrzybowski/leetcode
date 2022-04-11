pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
    let mut i = 0;
    for index in 0..nums.len() {
        if nums[index] != val {
            nums[i] = nums[index];
            i += 1;
        }
    }
    i as i32
}
