/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = {};
    for (let i = 0; i < nums.length; i++){
        needed = target - nums[i];
        if (needed in seen) {
            return [seen[needed], i];
        }
        seen[nums[i]] = i;
    }
};