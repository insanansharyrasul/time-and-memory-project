#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include </home/teaguy21/Documents/plotting/CPP/constant.h>
using namespace std;

int getFirstElement(const vector<int> &arr)
{
    return arr[0];
}

int main()
{
    vector<int> inputArray;
    int amount = N_VALUE;

    for (int i = 0; i < amount; i++) {
        inputArray.push_back(rand() % amount);
    }

    auto start = chrono::high_resolution_clock::now();
    getFirstElement(inputArray);
    auto end = chrono::high_resolution_clock::now();
    
    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
    cout << fixed << setprecision(9) << duration.count()/1000000000.0 << endl;
    return 0;
}
