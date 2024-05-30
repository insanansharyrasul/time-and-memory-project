function binarySearch(arr, x)
{    
    let low = 0;
    let high = arr.length - 1;
    let mid;
    while (high >= low) {
         mid = low + Math.floor((high - low) / 2);
 
        // If the element is present at the middle
        // itself
        if (arr[mid] == x)
            return mid;
 
        // If element is smaller than mid, then
        // it can only be present in left subarray
        if (arr[mid] > x)
            high = mid - 1;
            
        // Else the element can only be present
        // in right subarray
        else 
            low = mid + 1;
    }
 
    // We reach here when element is not
    // present in array
    return -1;
}

const myModule = require('/home/teaguy21/Documents/memory_test/constant/constant.js');

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

// if (result !== -1) {
//   console.log(`Element is present at index ${result}`);
// } else {
//   console.log("Element is not present in array");
// }
