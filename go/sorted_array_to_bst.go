package algos

func sortedArrayRanged(nums []int, left int, right int) *TreeNode {
	if right > left {
		return nil
	} else if left == right {
		return &TreeNode{Val: nums[left]}
	} else if right-left == 1 {
		return &TreeNode{
			Val:  nums[right],
			Left: &TreeNode{Val: nums[left]},
		}
	} else if right-left == 2 {
		return &TreeNode{
			Val:   nums[left+1],
			Left:  &TreeNode{Val: nums[left]},
			Right: &TreeNode{Val: nums[right]},
		}
	} else {
		middle := left + (right-left)/2
		return &TreeNode{
			Val:   nums[middle],
			Left:  sortedArrayRanged(nums, left, middle-1),
			Right: sortedArrayRanged(nums, middle+1, right),
		}
	}
}

func sortedArrayToBST(nums []int) *TreeNode {
	return sortedArrayRanged(nums, 0, len(nums)-1)
}
