var twoSum = function(nums, target) {
     for (let i = 0; i < nums.length; i++) {
         const compliment = target - nums[i];
         if (compliment in map) {
             return [map[compliment], i]
         }
         map[nums[i]] = i
     }
 };