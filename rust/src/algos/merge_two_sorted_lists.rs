#[derive(PartialEq, Eq, Debug)]
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

pub fn merge_two_lists(
    list1: Option<Box<ListNode>>,
    list2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    match (list1, list2) {
        (None, None) => None,
        (None, Some(list2)) => Some(list2),
        (Some(list1), None) => Some(list1),
        (Some(list1), Some(list2)) => {
            if list1.val <= list2.val {
                let mut result = list1;
                result.next = merge_two_lists(result.next, Some(list2));
                Some(result)
            } else {
                let mut result = list2;
                result.next = merge_two_lists(Some(list1), result.next);
                Some(result)
            }
        }
    }
}

pub fn merge_two_lists_iterative(
    list1: Option<Box<ListNode>>,
    list2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {

    let mut result = Box::new(ListNode::new(0));
    let mut pointer = &mut result;

    let mut first = list1;
    let mut second = list2;


    while first.is_some() && second.is_some() {
       let first_taken = first.take();
       let second_taken = second.take();

        if let (Some(mut first_head), Some(mut second_head)) = (first_taken, second_taken) {
            if first_head.val <= second_head.val {
                first = first_head.next.take();
                second = Some(second_head);
                pointer = pointer.next.get_or_insert(first_head);
            } else {
                second = second_head.next.take();
                first = Some(first_head);
                pointer = pointer.next.get_or_insert(second_head);
            }
        }
    }

    if first.is_some() {
        pointer.next = first;
    }
    if second.is_some(){
        pointer.next = second;
    }
    result.next
}
