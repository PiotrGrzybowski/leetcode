pub fn length_of_last_word(s: String) -> i32 {
    let chars: Vec<char> = s.chars().collect();
    let mut index: i32 = (chars.len() as i32) - 1;

    while chars[index as usize] == ' ' {
        index -= 1;
    }
    let pointer = index;
    while index >= 0 && chars[index as usize] != ' ' {
        index -= 1;
    }

    (pointer - index) as i32
}
