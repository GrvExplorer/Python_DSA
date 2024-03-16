var sortedSquares = function(nums) {
    let squreNums = nums.map((v) =>  v*v)
    let sortAndSquareNums = squreNums.sort((a, b) => a-b)
    return sortAndSquareNums
};



const ans = [-4, -1, 0, 3, 10]
console.log(sortedSquares([-4, -1, 0, 3, 10]));