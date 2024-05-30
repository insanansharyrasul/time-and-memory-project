import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Random;
import java.util.Scanner;

public class nsquare {

    static void bubbleSort(int arr[], int n) {
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++) {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {

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

    static void printArray(int arr[], int size) {
        int i;
        for (i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) throws FileNotFoundException {
        Scanner reader = new Scanner(new File("/home/teaguy21/Documents/memory_test/constant/constant.txt"));
        int myNumber = reader.nextInt();
        reader.close();
        int amount = myNumber;
        int[] arr = new int[amount];
        Random rand = new Random();
        for (int i = 0; i < amount; i++) {
            arr[i] = rand.nextInt(amount);
        }
        int n = arr.length;

        long start = System.nanoTime();
        bubbleSort(arr, n);
        long end = System.nanoTime();
        BigDecimal d = new BigDecimal((end - start)/ 1000000000.0).setScale(6, RoundingMode.HALF_EVEN);
        System.out.println(d);
        // System.out.println("Sorted array: ");
        // printArray(arr, n);
    }
}
