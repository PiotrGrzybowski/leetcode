pub fn is_palindrome(x: i32) -> bool {
    let mut number = x;
    if number < 0 || (number % 10 == 0 && x != 0) {
        false
    } else {
        let mut reversed = 0;
        while number > reversed {
            reversed = reversed * 10 + number % 10;
            number /= 10;
        }
        number == reversed || number == reversed / 10
    }
}
