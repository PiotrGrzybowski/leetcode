use std::io::Read;

struct Node {
    value: i32,
    next: Option<Box<Node>>,
}

impl Node {
    pub fn new(value: i32) -> Self {
        Node { value, next: None }
    }
}

pub struct MinStack {
    top: Option<Box<Node>>,
    minimum: i32,
}

impl MinStack {
    pub fn new() -> Self {
        MinStack { top: None, minimum: 0 }
    }

    pub fn push(&mut self, val: i32) {
        let mut node = Box::new(Node::new(val));
        match &self.top {
            Some(top) => {
                // node.next = Some(top);
            }
            None => {
                self.top = Some(node)
            }
        }
        if val < self.minimum {
            self.minimum = val
        }
    }

    pub fn pop(&self) {

    }

    pub fn top(&self) -> i32 {
        match &self.top {
            Some(top) => top.value,
            None => -1
        }
    }

    pub fn get_min(&self) -> i32 {
        self.minimum
    }
}

