function countSort(inputArray) {
    const N = inputArray.length;
    let M = 0;

    for (let i = 0; i < N; i++) {
        M = Math.max(M, inputArray[i]);
    }
    const countArray = new Array(M + 1).fill(0);

    for (let i = 0; i < N; i++) {
        countArray[inputArray[i]]++;
    }

    for (let i = 1; i <= M; i++) {
        countArray[i] += countArray[i - 1];
    }

    const outputArray = new Array(N);
    for (let i = N - 1; i >= 0; i--) {
        outputArray[countArray[inputArray[i]] - 1] = inputArray[i];
        countArray[inputArray[i]]--;
    }

    return outputArray;
}

const {performance} = require('perf_hooks');
const myModule = require('/home/teaguy21/Documents/memory_test/constant/constant.js');
const inputArray = []
let amount = myModule.myVariable
for (let i = 0; i < amount; i++) {
    inputArray.push(Math.floor(Math.random() * amount) + 1)
  }

let start = performance.now()
countSort(inputArray)
let end = performance.now()

console.log(((end - start)/1000).toFixed(6))
