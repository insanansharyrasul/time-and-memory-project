#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include </home/teaguy21/Documents/memory_test/constant/constant.h>
using namespace std;

// An iterative binary search function.
int binarySearch(vector<int> arr, int low, int high, int x)
{
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == x)
            return mid;

        if (arr[mid] < x)
            low = mid + 1;

        else
            high = mid - 1;
    }
    return -1;
}

// Driver code
int main(void)
{
    vector<int> arr;
    int amount = N_VALUE; 
    for (int i = 1; i <= amount; i++)
    {
        arr.push_back(i);
    }
    int x = 1;
    int n = arr.size();

    auto start = chrono::high_resolution_clock::now();
    int result = binarySearch(arr, 0, n - 1, x);
    auto end = chrono::high_resolution_clock::now();

    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
    cout << fixed << setprecision(9) << duration.count() / 1000000000.0 << endl;
    // (result == -1)
    //     ? cout << "Element is not present in array"
    //     : cout << "Element is present at index " << result;
    return 0;
}