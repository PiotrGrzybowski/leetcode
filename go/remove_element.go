package algos

func removeElement(nums []int, val int) int {
	i := 0
	for index := 0; index < len(nums); index++ {
		if nums[index] != val {
			nums[i] = nums[index]
			i += 1
		}
	}
	return i
}