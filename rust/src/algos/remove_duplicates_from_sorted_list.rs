#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

pub fn remove_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    if head.is_none() {
        return None;
    }
    let mut taken_head = head;
    let mut pointer = taken_head.as_mut().unwrap();
    while let Some(taken_pointer) = pointer.next.as_mut() {
        if pointer.val == taken_pointer.val {
            pointer.next = taken_pointer.next.take();
        } else {
            pointer = pointer.next.as_mut().unwrap();
        }
    }
    taken_head
}
