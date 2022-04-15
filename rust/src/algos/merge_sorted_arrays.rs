pub fn merge(first: &mut Vec<i32>, m: i32, second: &mut Vec<i32>, n: i32) -> Vec<i32> {
    let mut first_index = m - 1;
    let mut second_index = n - 1;
    let mut target_index = m + n - 1;

    while second_index >= 0 {
        if first_index >= 0 && first[first_index as usize] > second[second_index as usize] {
            first[target_index as usize] = first[first_index as usize];
            first_index -= 1;
            target_index -= 1;
        } else {
            first[target_index as usize] = second[second_index as usize];
            second_index -= 1;
            target_index -= 1;
        }
    }
    first.clone()
}
