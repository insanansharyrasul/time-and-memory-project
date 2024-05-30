import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Random;
import java.util.Scanner;

public class one {
	static int getFirstElement(int[] array) {
		return array[0];
	}

	public static void main(String[] args) throws FileNotFoundException{
		Scanner reader = new Scanner(new File("/home/teaguy21/Documents/exp/constant.txt"));
        int myNumber = reader.nextInt();
        reader.close();
		int amount = myNumber;
		int[] inputArray = new int[amount];
		Random rand = new Random();
		for (int i = 0; i < amount; i++) {
			inputArray[i] = rand.nextInt(amount);
		}

		long start = System.nanoTime();
		getFirstElement(inputArray);
		long end = System.nanoTime();
		BigDecimal d = new BigDecimal((end - start) / 1000000000.0).setScale(6, RoundingMode.HALF_EVEN);
		System.out.println(d);
	}
}
