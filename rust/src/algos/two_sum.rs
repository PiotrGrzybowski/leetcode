use std::collections::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    if nums.len() == 0 || nums[0] + nums[1] == target {
        vec![0, 1]
    } else {
        let mut cache: HashMap<i32, i32> =
            HashMap::from([(target - nums[0], 0), (target - nums[1], 1)]);
        let mut index = 2;
        while index < nums.len() && !cache.contains_key(&nums[index]) {
            cache.insert(target - nums[index], index as i32);
            index += 1;
        }
        vec![*cache.get(&nums[index]).unwrap(), index as i32]
    }
}
