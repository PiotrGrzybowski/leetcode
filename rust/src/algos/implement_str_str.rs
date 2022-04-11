pub fn str_str(haystack: String, needle: String) -> i32 {
    if needle.len() == 0 {
        return 0;
    }
    if needle.len() > haystack.len() {
        return -1
    }
    let haystack_chars: Vec<char> = haystack.chars().collect();
    let needle_chars: Vec<char> = needle.chars().collect();
    let mut index = 0;
    while index <= haystack_chars.len() - needle_chars.len() {
        let mut i = 0;

        while i < needle_chars.len() && haystack_chars[index + i] == needle_chars[i] {
            i += 1;
        }
        if i == needle_chars.len() {
            return index as i32
        }
        index += 1
    }
    -1
}
