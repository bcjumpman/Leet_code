/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  // arr[]
  let arr = [];

  // for loop n
  //      2
  for (let i = 0; i < nums.length; i++) {
    // for loop m
    //       7
    for (let j = 1; j < nums.length; j++) {
      //      2  +     7  ==== 9
      if (nums[i] + nums[j] === target) {
        // 0
        arr.push(i);
        // 1
        arr.push(j);

        //     [0,1]
        return arr;
      }
    }
  }

  // ind[v]

  // returning both indices
};

console.log(twoSum([2, 7, 11, 15], 9));
