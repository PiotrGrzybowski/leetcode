package algos

func removeDuplicates(nums []int) int {
	i := 0
	for j := 0; j < len(nums); j++ {
		if nums[i] != nums[j] {
			i += 1
			nums[i] = nums[j]
		}
	}
	return i + 1
}
