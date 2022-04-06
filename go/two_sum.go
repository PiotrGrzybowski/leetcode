package algos

import "fmt"

func twoSum(nums []int, target int) []int {
	if len(nums) == 2 {
		return []int{0, 1}
	} else if nums[0]+nums[1] == target {
		return []int{0, 1}
	} else {
		cache := make(map[int]int)
		cache[target-nums[0]] = 0
		cache[target-nums[1]] = 1
		fmt.Println(cache)
		for i := 2; i < len(nums); i++ {
			if _, ok := cache[nums[i]]; ok {
				return []int{cache[nums[i]], i}
			} else {
				cache[target-nums[i]] = i
			}
		}
	}
	return []int{0, 1}
}
