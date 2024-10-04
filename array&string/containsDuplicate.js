/**
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]

Output: true
Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.

Example 3:
Input: nums = []
Output: true

Example 4:
Input: nums = [1, 4.5]
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

//  * @param {number[]} nums
//  * @return {boolean}
 */

const hasDuplicate = (nums) => {
  const dup = {}; // {1:true, 2:true, 3:true}
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i]; //3
    if (dup[num]) return true;
    dup[num] = true;
  }
  return false;
};
