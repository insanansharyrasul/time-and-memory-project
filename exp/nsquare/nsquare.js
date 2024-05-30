function bubbleSort(arr, n)
{
    var i, j, temp;
    var swapped;
    for (i = 0; i < n - 1; i++) 
    {
        swapped = false;
        for (j = 0; j < n - i - 1; j++) 
        {
            if (arr[j] > arr[j + 1]) 
            {
                
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        if (swapped == false)
        break;
    }
}


// function printArray(arr, size)
// {
//   var i;
//   for (i = 0; i < size; i++)
//       console.log(arr[i] + " ");
// }

const {performance} = require('perf_hooks');

const arr = []
const myModule = require('/home/teaguy21/Documents/exp/constant.js');
let amount = myModule.myVariable
for (let i = 0; i < amount; i++) {
    arr.push(Math.floor(Math.random() * amount) + 1)
  }
var n = arr.length;

let start = performance.now()
bubbleSort(arr, n);
let end = performance.now()
// console.log("Sorted array: ");
// printArray(arr, n);
console.log(((end - start)/1000).toFixed(6))