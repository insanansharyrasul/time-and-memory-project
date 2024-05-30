function getFirstElement(arr) {
    return arr[0];
}

const {performance} = require('perf_hooks');
function main() {
    const inputArray = []
    const myModule = require('/home/teaguy21/Documents/memory_test/constant/constant.js');
    let amount = myModule.myVariable
    for (let i = 0; i < amount; i++) {
        inputArray.push(Math.floor(Math.random() * amount) + 1)
    }

    let start = performance.now()
    getFirstElement(inputArray)
    let end = performance.now()

    console.log((((end - start)/1000).toFixed(6)))
    // console.log("The first element is: " + result);
}

main();