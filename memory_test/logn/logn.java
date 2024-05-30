import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

public class logn {
    // Returns index of x if it is present in arr[].
    int binarySearch(int arr[], int x) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;

            // Check if x is present at mid
            if (arr[mid] == x)
                return mid;

            // If x greater, ignore left half
            if (arr[mid] < x)
                low = mid + 1;

            // If x is smaller, ignore right half
            else
                high = mid - 1;
        }

        // If we reach here, then element was
        // not present
        return -1;
    }

    // Driver code
    public static void main(String args[]) throws FileNotFoundException {
        Scanner reader = new Scanner(new File("/home/teaguy21/Documents/memory_test/constant/constant.txt"));
        int myNumber = reader.nextInt();
        reader.close();
        logn ob = new logn();
        int amount = myNumber;
        int[] inputArray = new int[amount];
        for (int i = 0; i < amount; i++) {
            inputArray[i] = i;
        }

        long start = System.nanoTime();
        ob.binarySearch(inputArray, 1);
        long end = System.nanoTime();
        BigDecimal d = new BigDecimal((end - start) / 1000000000.0).setScale(6, RoundingMode.HALF_EVEN);
        System.out.println(d);
        // if (result == -1)
        // System.out.println(
        // "Element is not present in array");
        // else
        // System.out.println("Element is present at "
        // + "index " + result);
    }
}
