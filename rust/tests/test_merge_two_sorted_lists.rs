use rust::algos::merge_two_sorted_lists::{ListNode, merge_two_lists, merge_two_lists_iterative};

#[test]
fn test_merge_two_sorted_lists_both_empty() {
    let list1: Option<Box<ListNode>> = None;
    let list2: Option<Box<ListNode>> = None;
    let result = merge_two_lists(list1, list2);

    assert_eq!(result, None);
}

#[test]
fn test_merge_two_sorted_lists_second_empty() {
    let list1: Option<Box<ListNode>> = None;
    let list2: Option<Box<ListNode>> = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode { val: 4, next: None })),
        })),
    }));
    let mut node = merge_two_lists(list2, list1).unwrap();
    assert_eq!(node.val, 1);

    node = node.next.unwrap();
    assert_eq!(node.val, 2);

    node = node.next.unwrap();
    assert_eq!(node.val, 4);

    assert_eq!(node.next, None);
}

#[test]
fn test_merge_two_sorted_lists_first_empty() {
    let list1: Option<Box<ListNode>> = None;
    let list2: Option<Box<ListNode>> = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode { val: 4, next: None })),
        })),
    }));
    let mut node = merge_two_lists(list1, list2).unwrap();
    assert_eq!(node.val, 1);

    node = node.next.unwrap();
    assert_eq!(node.val, 2);

    node = node.next.unwrap();
    assert_eq!(node.val, 4);

    assert_eq!(node.next, None);
}

#[test]
fn test_merge_two_sorted_lists_both_not_empty() {
    let list1: Option<Box<ListNode>> = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode { val: 4, next: None })),
        })),
    }));
    let list2: Option<Box<ListNode>> = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 3,
            next: Some(Box::new(ListNode { val: 4, next: None })),
        })),
    }));
    let mut node = merge_two_lists(list1, list2).unwrap();
    assert_eq!(node.val, 1);

    node = node.next.unwrap();
    assert_eq!(node.val, 1);

    node = node.next.unwrap();
    assert_eq!(node.val, 2);

    node = node.next.unwrap();
    assert_eq!(node.val, 3);

    node = node.next.unwrap();
    assert_eq!(node.val, 4);

    node = node.next.unwrap();
    assert_eq!(node.val, 4);

    assert_eq!(node.next, None);
}

#[test]
fn test_merge_two_sorted_lists_both_not_empty_iterative() {
    let list1: Option<Box<ListNode>> = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode { val: 4, next: None })),
        })),
    }));
    let list2: Option<Box<ListNode>> = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 3,
            next: Some(Box::new(ListNode { val: 4, next: None })),
        })),
    }));
    let mut node = merge_two_lists_iterative(list1, list2).unwrap();
    assert_eq!(node.val, 1);

    node = node.next.unwrap();
    assert_eq!(node.val, 1);

    node = node.next.unwrap();
    assert_eq!(node.val, 2);

    node = node.next.unwrap();
    assert_eq!(node.val, 3);

    node = node.next.unwrap();
    assert_eq!(node.val, 4);

    node = node.next.unwrap();
    assert_eq!(node.val, 4);

    assert_eq!(node.next, None);

    // let mut first = &list1;
    // println!("{:?}", first);
    //
    // // first = &(*first).as_ref().unwrap().next;
    // first = &first.as_ref().unwrap().next;
    // println!("{:?}", first);
}
