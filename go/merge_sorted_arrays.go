package algos

func merge(first []int, m int, second []int, n int) []int {
    first_index := m - 1
    second_index := n - 1
    target_index := m + n - 1

    for second_index >= 0 {
        if first_index >= 0 && first[first_index] > second[second_index] {
            first[target_index] = first[first_index]
            first_index -= 1
        } else {
            first[target_index] = second[second_index]
            second_index -= 1
        }
        target_index -= 1
    }
    return first
}


