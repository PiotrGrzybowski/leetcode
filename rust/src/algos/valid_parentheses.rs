use std::collections::{HashMap, LinkedList};

pub fn valid_parentheses(expression: String) -> bool {
    let mut stack = LinkedList::new();
    let mapping = HashMap::from([(')', '('), ('}', '{'), (']', '[')]);

    for sign in expression.chars() {
        if is_left(sign) {
            stack.push_back(sign);
        } else {
            if stack.is_empty() || stack.back().unwrap() != mapping.get(&sign).unwrap() {
                return false;
            } else {
                stack.pop_back();
            }
        }
    }
    stack.is_empty()
}

fn is_left(sign: char) -> bool {
    sign == '(' || sign == '[' || sign == '{'
}