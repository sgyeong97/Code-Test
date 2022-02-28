var largestPerimeter = function(nums) {
    nums.sort((a,b) => b-a);
    const limit = nums.length - 2;
    for (let x = 0; x < limit; x++){
        if(nums[x] < nums[x+1]+nums[x+2]){
            return nums[x]+nums[x+1]+nums[x+2];
        }
    }
    return 0;
};