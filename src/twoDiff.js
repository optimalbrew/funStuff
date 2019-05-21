// Kash: find indices of pairs from list such that the difference is equal to a target

function twoDiff(nums, target){
    sol=[];
    for (var i=0; i < nums.length-1;i++){                
        for (var j=1; j < nums.length;j++){
            if (nums[j] - nums[i]==target){
                //console.log(i,j);
                sol.push([i,j]);
            }
        }        
    }        
    return sol;
}
    
#simple test
var nums = [1,2,3,4,2];
var target = 1;

twoDiff(nums,target)