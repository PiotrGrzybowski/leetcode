use std::collections::HashMap;

pub fn roman_to_int(s: String) -> i32 {
    let map = HashMap::from([
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000),
    ]);
    let mut previous = 0;
    let mut result = 0;
    for c in s.chars().rev() {
        let value = *map.get(&c).unwrap();
        if value >= previous {
            result += value;
        } else {
            result -= value;
        }
        previous = value;
    }
    result
}
