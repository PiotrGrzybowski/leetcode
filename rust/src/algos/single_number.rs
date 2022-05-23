use std::collections::HashMap;

pub fn single_number(numbers: Vec<i32>) -> i32 {
    let mut occurrences: HashMap<i32, i32> = HashMap::new();
    for number in numbers.iter() {
        *occurrences.entry(*number).or_insert(0) += 1;
    }
    for (key, number) in occurrences.iter() {
        if *number == 1 {
            return *key
        }
    }
    0
}