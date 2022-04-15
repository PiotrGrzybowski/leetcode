pub fn climb_stairs(stairs: i32) -> i32 {
    if stairs == 1 {
        1
    } else if stairs == 2 {
        2
    } else {
        let mut n = stairs;
        let mut last = 2;
        let mut earlier = 1;
        let mut answer = 0;
        while n > 2 {
            answer = last + earlier;
            earlier = last;
            last = answer;
            n -= 1;
        }
        answer
    }
}
