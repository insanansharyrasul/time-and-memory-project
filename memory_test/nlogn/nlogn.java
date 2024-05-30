import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Random;
import java.util.Scanner;

public class nlogn {

    void merge(int arr[], int l, int m, int r) {

        int n1 = m - l + 1;
        int n2 = r - m;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];

        int i = 0, j = 0;

        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    void sort(int arr[], int l, int r) {
        if (l < r) {

            int m = l + (r - l) / 2;

            sort(arr, l, m);
            sort(arr, m + 1, r);

            merge(arr, l, m, r);
        }
    }

    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
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

        nlogn ob = new nlogn();

        long start = System.nanoTime();
        ob.sort(arr, 0, arr.length - 1);
        long end = System.nanoTime();
        BigDecimal d = new BigDecimal((end - start) / 1000000000.0).setScale(6, RoundingMode.HALF_EVEN);
        System.out.println(d);

    }
}