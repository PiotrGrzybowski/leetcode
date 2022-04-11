pub fn my_sqrt(x: i32) -> i32 {
    if x == 0 {
        0
    } else if x < 4 {
        1
    } else {
        let mut left = 1;
        let mut right = x / 2;
        let mut result = 0;

        while left <= right {
            let middle = left + (right - left) / 2;
            if middle <= x / middle {
                left = middle + 1;
                result = middle;
            } else {
                right = middle - 1;
            }
        }
        result
    }
}
