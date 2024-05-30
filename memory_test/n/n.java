import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Random;
import java.util.Scanner;

public class n {
	public static int[] countSort(int[] inputArray) {
		int N = inputArray.length;
		int M = 0;
		for (int i = 0; i < N; i++) {
			M = Math.max(M, inputArray[i]);
		}

		int[] countArray = new int[M + 1];

		for (int i = 0; i < N; i++) {
			countArray[inputArray[i]]++;
		}

		for (int i = 1; i <= M; i++) {
			countArray[i] += countArray[i - 1];
		}

		int[] outputArray = new int[N];

		for (int i = N - 1; i >= 0; i--) {
			outputArray[countArray[inputArray[i]] - 1] = inputArray[i];
			countArray[inputArray[i]]--;
		}

		return outputArray;
	}

	public static void main(String[] args) throws FileNotFoundException {
		Scanner reader = new Scanner(new File("/home/teaguy21/Documents/memory_test/constant/constant.txt"));
        int myNumber = reader.nextInt();
        reader.close();
		int amount = myNumber;
		int[] inputArray = new int[amount];
		Random rand = new Random();
		for (int i = 0; i < amount; i++) {
			inputArray[i] = rand.nextInt(amount);
		}

		long start = System.nanoTime();
		countSort(inputArray);
		long end = System.nanoTime();
		BigDecimal d = new BigDecimal((end - start)/1000000000.0).setScale(6, RoundingMode.HALF_EVEN);
		System.out.println(d);
	}
}
