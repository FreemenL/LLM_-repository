// 给定一个含有 n 个正整数 的数组和一个正整数 target。
// 找出该数组中满足其和 ≥ target 的长度最小的连续子数组，并返回其长度。
// 如果不存在符合条件的子数组，返回 0。
 
// 示例 1
// 输入： target = 7 ,  nums = [2,3,1,2,4,3] 
// 输出： 2 
// 解释：子数组  [4,3]  是该条件下的长度最小的子数组。
 
// 示例 2
// 输入： target = 11 ,  nums = [1,1,1,1,1,1,1,1] 
// 输出： 0


function getResult(array,target){
    if(!Array.isArray(array)){
        throw Error('array must be an array');
    }
    let cacheNumner = 0;
    let account =0 ;
    for (let i = 0;i<array.length;i++){
        for(let j= 0;j<array.length;j++){
                cacheNumner = array[i]+array[j];
                account+=1;
                if(cacheNumner===target){  
                    return account;
                }
        }
    }  
    return 0;
}

let target = 7;
let  nums = [2,3,1,2,4,3];
const result = getResult(nums,target);
console.log(result);





