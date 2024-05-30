#include <cstdlib>
#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include </home/teaguy21/Documents/plotting/CPP/constant.h>
using namespace std;

vector<int> countSort(vector<int> &inputArray)
{
    int N = inputArray.size();
    int M = 0;
    for (int i = 0; i < N; i++)
        M = max(M, inputArray[i]);
    vector<int> countArray(M + 1, 0);
    for (int i = 0; i < N; i++)
        countArray[inputArray[i]]++;
    for (int i = 1; i <= M; i++)
        countArray[i] += countArray[i - 1];
    vector<int> outputArray(N);
    for (int i = N - 1; i >= 0; i--)
    {
        outputArray[countArray[inputArray[i]] - 1] = inputArray[i];
        countArray[inputArray[i]]--;
    }
    return outputArray;
}

int main()
{
    vector<int> inputArray;
    int amount = N_VALUE;

    for (int i = 0; i < amount; i++)
    {
        inputArray.push_back(rand() % amount);
    }

    auto start = chrono::high_resolution_clock::now();
    countSort(inputArray);
    auto end = chrono::high_resolution_clock::now();

    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
    cout << fixed << setprecision(9) << duration.count() / 1000000000.0 << endl;
    return 0;
}