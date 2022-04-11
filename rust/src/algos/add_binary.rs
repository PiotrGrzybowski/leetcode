pub fn add_binary(a: String, b: String) -> String {
    let first: String;
    let second: String;
    if a.len() < b.len() {
        second = a;
        first = b;
    } else {
        first = a;
        second = b;
    }

    let first_digits: Vec<char> = first.chars().rev().collect();
    let second_digits: Vec<char> = second.chars().rev().collect();

    let mut i = 0;
    let mut result = String::new();
    let mut overflow = false;

    while i < second_digits.len() {
        if first_digits[i] == '0' && second_digits[i] == '0' {
            if !overflow {
                result.push('0');
            } else {
                result.push('1');
                overflow = false;
            }
        } else if first_digits[i] == '1' && second_digits[i] == '1' {
            if !overflow {
                result.push('0');
                overflow = true;
            } else {
                result.push('1');
                overflow = true;
            }
        } else {
            if !overflow {
                result.push('1');
            } else {
                result.push('0');
                overflow = true;
            }
        }
        i += 1;
    }

    while i < first_digits.len() {
        if first_digits[i] == '0' {
            if !overflow {
                result.push('0');
            } else {
                result.push('1');
                overflow = false;
            }
        } else {
            if !overflow {
                result.push('1');
            } else {
                result.push('0');
                overflow = true;
            }
        }
        i += 1;
    }
    if overflow {
        result.push('1');
    }

    result.chars().rev().collect()
}