function binarySearch(arr, x)
{    
    let low = 0;
    let high = arr.length - 1;
    let mid;
    while (high >= low) {
         mid = low + Math.floor((high - low) / 2);
 
        if (arr[mid] == x)
            return mid;
 
        if (arr[mid] > x)
            high = mid - 1;
            
        else 
            low = mid + 1;
    }
 
    return -1;
}

const myModule = require('/home/teaguy21/Documents/exp/constant.js');

const arr = [];
for (let i = 1; i <= myModule.myVariable; i++) {
  arr.push(i);
}

const {performance} = require('perf_hooks');
const x = 1;

const startTime = performance.now(); 
const result = binarySearch(arr, x);
const endTime = performance.now();

console.log(`${((endTime - startTime) / 1000).toFixed(6)}s`);

