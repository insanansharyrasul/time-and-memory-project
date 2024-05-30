#include <array>
#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include </home/teaguy21/Documents/exp/constant.h>
using namespace std;

void bubbleSort(vector<int> &arr, int n)
{
    int i, j;
    bool swapped;
    for (i = 0; i < n - 1; i++)
    {
        swapped = false;
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        if (swapped == false)
            break;
    }
}

void printArray(vector<int> &arr, int size)
{
    int i;
    for (i = 0; i < size; i++)
        cout << " " << arr[i];
}

int main()
{
    vector<int> arr;
    int amount = N_VALUE;

    for (int i = 0; i < amount; i++)
    {
        arr.push_back(rand() % amount);
    }

    auto start = chrono::high_resolution_clock::now();
    bubbleSort(arr, arr.size());
    auto end = chrono::high_resolution_clock::now();

    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
    cout << fixed << setprecision(9) << duration.count() / 1000000000.0 << endl;
    return 0;
}